import os
import shutil

import pandas as pd
import torch
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from tqdm import tqdm
from pandarallel import pandarallel
import cv2
from PIL import Image, ImageFile
import imghdr
import numpy as np
import argparse

"""
    参考如下的数据格式：
    - D:/xianghongxin/work/projects/MultiViewMolKD/datasets/fine-tuning/mpp/bace
        - processed
            - image
            - video
            - bace_processed_ac.csv
            - geometric_data_processed.pt
"""


def is_img(path):
    if not os.path.exists(path):
        return False
    try:
        img = cv2.imread(path)
        img.shape
        return True
    except:
        os.remove(path)
        return False


def padding_resize_func(src, trt):
    # if os.path.exists(trt):
    #     img = cv2.imread(trt)
    #     try:
    #         img.shape
    #     except:
    #         print(trt)
    # os.remove(path)
    # padding and resize
    img = padding_white(src, 640, 640)
    img = Image.fromarray(img.astype(np.uint8))
    out = img.resize((224, 224), Image.ANTIALIAS)
    out.save(trt)


def to_canonical_smiles(smiles):
    m = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(m, canonical=True)


def read_dataset_csv(dataset, raw_csv_path, processed_csv_path):
    if "esol" in dataset:
        label_name = 'measured log solubility in mols per litre'
    elif "lipophilicity" in dataset:
        label_name = 'exp'
    elif "cep" in dataset:
        label_name = 'PCE'
    elif "malaria" in dataset:
        label_name = 'activity'
    else:
        label_name = 'label'
        # raise NotImplementedError

    df_raw = pd.read_csv(raw_csv_path)
    df_processed = pd.read_csv(processed_csv_path, names=["smiles"])

    df_raw["index"] = range(1, df_raw.shape[0] + 1)
    df_raw["label"] = df_raw[label_name]
    df_raw["canonical_smiles"] = df_raw["smiles"].apply(lambda x: to_canonical_smiles(x))
    df_raw = df_raw[["index", "smiles", "canonical_smiles", "label"]]

    assert df_raw["smiles"].tolist() == df_processed["smiles"].tolist()
    df_processed = df_raw

    return df_raw, df_processed


def Smiles2Img(smis, size=224, savePath=None):
    '''
        smis: e.g. COC1=C(C=CC(=C1)NS(=O)(=O)C)C2=CN=CN3C2=CC=C3
        path: E:/a/b/c.png
    '''
    try:
        mol = Chem.MolFromSmiles(smis)
        img = Draw.MolsToGridImage([mol], molsPerRow=1, subImgSize=(size, size))
        if savePath is not None:
            img.save(savePath)
        return img
    except:
        return None


def generate_and_save_3d_sdfs(smiles, path, randomSeed=0):
    """generate and save 3d sdfs

    Args:
        mol (rdkit.mol): molecule from rdkit
        smiles (str): smiles
        w (int): width
        h (int): height
        path (str): path to save image

    Returns:
        Returns 0 if the conformer of `mol` is converged
    """
    mol = Chem.MolFromSmiles(smiles)
    m3d = Chem.AddHs(mol)

    # single conformer
    try:
        try:
            AllChem.EmbedMolecule(m3d, randomSeed=randomSeed)
            res = AllChem.MMFFOptimizeMolecule(m3d, mmffVariant="MMFF94s", maxIters=10000)
        except:
            # issue: https://github.com/rdkit/rdkit/issues/1433 (conformations not generated for some molecules)
            print(
                "{} fails to generate, using random coordinates instead of eigenvalues of the distance matrix.".format(
                    smiles))
            AllChem.EmbedMolecule(m3d, useRandomCoords=True, randomSeed=randomSeed)
            res = AllChem.MMFFOptimizeMolecule(m3d, mmffVariant="MMFF94s", maxIters=10000)
    except:
        print(f"[{smiles}] save 2d sdf, because the 3d conformer can not be optimized")
        Chem.MolToMolFile(mol, path)
        return
    m3d = Chem.RemoveHs(m3d)
    Chem.MolToMolFile(m3d, path)


def padding_white(img_path, new_h, new_w):
    """
    white background to fill
    :return:
    """
    # 有时会报 libpng error: Read Error, 参见：https://blog.csdn.net/pku_langzi/article/details/122186071：用 Image 读取然后转化到 opencv 读取
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    if imghdr.what(img_path) == "png":
        Image.open(img_path).convert("RGB").save(img_path)

    # cv2 是以 BGR 通道的顺序进行读取的，因此需要转化为 RGB 的形式。
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将图像从 BGR 格式转换为 RGB 格式

    h, w, c = img.shape

    new_img = np.ones(shape=(new_h, new_w, 3)) * 255  # fill white: (255, 255, 255)

    assert (new_w - w) % 2 == 0 and (new_h - h) % 2 == 0
    left, right, top, bottom = (new_w - w) // 2, (new_w - w) // 2 + w, (new_h - h) // 2, (new_h - h) // 2 + h
    new_img[top:bottom, left:right] = img

    return new_img


def resize_shape(img_path, new_w, new_h, savepath):
    im = Image.open(img_path)
    out = im.resize((new_w, new_h), Image.ANTIALIAS)
    out.save(savepath)


def step2_generate_images(dataset, work_dir):
    processed_dir = f"{work_dir}/processed"
    processed_csv_path = f"{processed_dir}/{dataset}_processed_ac.csv"
    df = pd.read_csv(processed_csv_path)

    save_image_root = f"{processed_dir}/image/"
    for index, smiles in tqdm(df[["index", "smiles"]].values.tolist()):
        if not os.path.exists(f"{save_image_root}/{index}"):
            os.makedirs(f"{save_image_root}/{index}")
        save_image_path = f"{save_image_root}/{index}/{index}.png"
        Smiles2Img(smiles, size=224, savePath=save_image_path)


def stub_generate_3d_sdf(series):
    generate_and_save_3d_sdfs(smiles=series.smiles, path=series.save_sdf_path, randomSeed=series.randomSeed)


def step3_generate_3d_sdfs(dataset, work_dir, randomSeed=0):
    processed_dir = f"{work_dir}/processed"
    processed_csv_path = f"{processed_dir}/{dataset}_processed_ac.csv"
    df = pd.read_csv(processed_csv_path)

    save_sdf_root = f"{processed_dir}/rdkit/seed{randomSeed}/sdfs"
    if not os.path.exists(save_sdf_root):
        os.makedirs(save_sdf_root)

    data_dict = {
        "smiles": [],
        "save_sdf_path": [],
        "randomSeed": []
    }
    for index, smiles in tqdm(df[["index", "smiles"]].values.tolist(), desc="generate 3d sdfs"):
        save_sdf_path = f"{save_sdf_root}/{index}.sdf"
        data_dict["smiles"].append(smiles)
        data_dict["save_sdf_path"].append(save_sdf_path)
        data_dict["randomSeed"].append(randomSeed)

    new_df = pd.DataFrame(data_dict)
    pandarallel.initialize(progress_bar=True)
    new_df.T.parallel_apply(stub_generate_3d_sdf)


def generate_4_views_image_by_pymol_640_224(series):
    import os
    # pymol = "C:/Users/user/AppData/Local/Schrodinger/PyMOL2/PyMOLWin.exe"
    # pymol = "/home/lzeng/xianghongxin/local/pymol/bin/pymol"
    pymol = "/home/xianghongxin/anaconda3/bin/pymol"  # 8_4090
    index, sdf_path, save_root, img_type = series["index"], series.sdf_path, series.save_root, series.img_type

    save_pml_root = f"{save_root}/pml-{img_type}/{index}"
    if not os.path.exists(save_pml_root):
        os.makedirs(save_pml_root)

    if img_type == "video":
        data = [("x_0", "rotate x, 0"), ("x_18", "rotate x, 18"), ("x_36", "rotate x, 36"), ("x_54", "rotate x, 54"), ("x_72", "rotate x, 72"), ("x_90", "rotate x, 90"), ("x_108", "rotate x, 108"), ("x_126", "rotate x, 126"), ("x_144", "rotate x, 144"), ("x_162", "rotate x, 162"), ("x_180", "rotate x, 180"), ("x_198", "rotate x, 198"), ("x_216", "rotate x, 216"), ("x_234", "rotate x, 234"), ("x_252", "rotate x, 252"), ("x_270", "rotate x, 270"), ("x_288", "rotate x, 288"), ("x_306", "rotate x, 306"), ("x_324", "rotate x, 324"), ("x_342", "rotate x, 342"), ("y_0", "rotate y, 0"), ("y_18", "rotate y, 18"), ("y_36", "rotate y, 36"), ("y_54", "rotate y, 54"), ("y_72", "rotate y, 72"), ("y_90", "rotate y, 90"), ("y_108", "rotate y, 108"), ("y_126", "rotate y, 126"), ("y_144", "rotate y, 144"), ("y_162", "rotate y, 162"), ("y_180", "rotate y, 180"), ("y_198", "rotate y, 198"), ("y_216", "rotate y, 216"), ("y_234", "rotate y, 234"), ("y_252", "rotate y, 252"), ("y_270", "rotate y, 270"), ("y_288", "rotate y, 288"), ("y_306", "rotate y, 306"), ("y_324", "rotate y, 324"), ("y_342", "rotate y, 342"), ("z_0", "rotate z, 0"), ("z_18", "rotate z, 18"), ("z_36", "rotate z, 36"), ("z_54", "rotate z, 54"), ("z_72", "rotate z, 72"), ("z_90", "rotate z, 90"), ("z_108", "rotate z, 108"), ("z_126", "rotate z, 126"), ("z_144", "rotate z, 144"), ("z_162", "rotate z, 162"), ("z_180", "rotate z, 180"), ("z_198", "rotate z, 198"), ("z_216", "rotate z, 216"), ("z_234", "rotate z, 234"), ("z_252", "rotate z, 252"), ("z_270", "rotate z, 270"), ("z_288", "rotate z, 288"), ("z_306", "rotate z, 306"), ("z_324", "rotate z, 324"), ("z_342", "rotate z, 342")]
    elif img_type == "IEM":
        data = [("x_0", "rotate x, 0.0"), ("x_180", "rotate x, 180.0"), ("y_180", "rotate y, 180.0"), ("z_180", "rotate z, 180.0")]
    else:
        raise NotImplementedError

    for axis_name, axis_pml in data:
        save_video_root = f"{save_root}/type-{img_type}-640x480/{index}"
        save_video_224_root = f"{save_root}/type-{img_type}/{index}"

        if not os.path.exists(save_video_root):
            os.makedirs(save_video_root)

        if not os.path.exists(save_video_224_root):
            os.makedirs(save_video_224_root)

        save_pml_path = f"{save_pml_root}/{axis_name}.pml"
        save_video_path = f"{save_video_root}/{axis_name}.png"
        save_video_224_path = f"{save_video_224_root}/{axis_name}.png"

        if is_img(save_video_224_path):
            continue

        if is_img(save_video_path):
            padding_resize_func(save_video_path, save_video_224_path)
            print("padding 640 to 224")
            continue

        # print(save_video_224_path)
        pml_command = f"load {sdf_path};bg_color white;set stick_ball,on;set stick_ball_ratio,3.5;" \
                      f"set stick_radius,0.15;set sphere_scale,0.2;set valence,1;set valence_mode,0;" \
                      f"set valence_size, 0.1;{axis_pml};save {save_video_path};quit"  # zoom all,1;

        with open(save_pml_path, "w") as f:
            f.write(pml_command)
        command = f"{pymol} -cKq {save_pml_path}"
        # print(command)
        os.system(command)

        # to 224
        padding_resize_func(save_video_path, save_video_224_path)
        os.remove(save_video_path)


def step4_generate_multiview_video_640_and_224(dataset, work_dir, img_type="video", randomSeed=0, platform="rdkit"):
    processed_dir = f"{work_dir}/processed"
    processed_csv_path = f"{processed_dir}/{dataset}_processed_ac.csv"
    df = pd.read_csv(processed_csv_path)

    index_list = []
    sdf_path_list = []
    save_root_list = []
    for index, smiles in tqdm(df[["index", "smiles"]].values.tolist()):
        sdf_path = f"{processed_dir}/{platform}/seed{randomSeed}/sdfs/{index}.sdf"

        index_list.append(index)
        sdf_path_list.append(sdf_path)
        save_root_list.append(f"{processed_dir}/{platform}/seed{randomSeed}")

    new_df = pd.DataFrame({
        "index": index_list,
        "sdf_path": sdf_path_list,
        "save_root": save_root_list,
        "img_type": img_type
    })

    multi_thread = True
    if multi_thread:
        pandarallel.initialize(progress_bar=True)
        new_df.T.parallel_apply(generate_4_views_image_by_pymol_640_224)
    else:
        for idx, series in tqdm(new_df.iterrows(), total=new_df.shape[0]):
            generate_4_views_image_by_pymol_640_224(series)

    shutil.rmtree(f"{processed_dir}/{platform}/seed{randomSeed}/type-{img_type}-640x480")

def step6_check(dataset, work_dir, img_type="IEM", randomSeed=0, platform="rdkit"):
    if img_type == "IEM":
        n_views = 4
    elif img_type == "video":
        n_views = 60
    else:
        raise NotImplementedError

    processed_dir = f"{work_dir}/processed"
    save_video_root = f"{processed_dir}/{platform}/seed{randomSeed}/type-{img_type}/"
    processed_csv_path = f"{processed_dir}/{dataset}_processed_ac.csv"
    df = pd.read_csv(processed_csv_path)
    assert len(os.listdir(save_video_root)) == df.shape[0]
    for index in tqdm(os.listdir(save_video_root), desc="check multi-view images"):
        assert len(os.listdir(f"{save_video_root}/{index}")) == n_views

    print("check success")
    return True


if __name__ == '__main__':
    """给一个 csv 文件，构建出数据集"""

    # csv_path = "StructureNet/acyclic_chain_molecules/CHEMBL348_MIC.csv"
    # saveroot = f"./processed_StructureNet/acyclic_chain_molecules"

    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str, help='')
    parser.add_argument('--saveroot', type=str, help='')
    args = parser.parse_args()

    csv_path = args.csv_path
    saveroot = args.saveroot

    filename = os.path.split(csv_path)[-1]
    dataset = filename.split(".")[0]

    raw_dir = f"{saveroot}/{dataset}/raw"
    processed_dir = f"{saveroot}/{dataset}/processed"

    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    df = pd.read_csv(csv_path)
    df.to_csv(f"{raw_dir}/{filename}", index=False)
    df.to_csv(f"{processed_dir}/{dataset}_processed_ac.csv", index=False)

    print(f"=========== processing {dataset} ===========")
    work_dir = f"./{saveroot}/{dataset}"
    # step2_generate_images(dataset, work_dir=f"{saveroot}/{dataset}")  # rdkit images

    # step3_generate_3d_sdfs(dataset, work_dir=f"{saveroot}/{dataset}", randomSeed=0)

    # step4_generate_multiview_video_640_and_224(dataset, work_dir=f"{saveroot}/{dataset}", img_type="IEM", randomSeed=0, platform="rdkit")
    step6_check(dataset, work_dir=f"{saveroot}/{dataset}", img_type="IEM")

    # step4_generate_multiview_video_640_and_224(dataset, work_dir=f"{saveroot}/{dataset}", img_type="video", randomSeed=0, platform="rdkit")
    step6_check(dataset, work_dir=f"{saveroot}/{dataset}", img_type="video")


