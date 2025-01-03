import sys
# sys.path.append("/data1/xianghongxin/work/mol-benchmarks")
sys.path.append("/tmp/pycharm_project_179")
import os
from argparse import ArgumentParser

import pandas as pd
import torch
from torch_geometric.data import InMemoryDataset
from tqdm import tqdm

from benchmol.data_process.molecules.graph_helpers.mol2_3dgraph import create_3d_graph_from_sdf


if __name__ == '__main__':
    # Parse arguments
    parser = ArgumentParser(description='PyTorch Implementation of FrameMol')
    parser.add_argument('--dataroot', type=str, default="reg_graphmvp_format/", help='path to exp folder')
    parser.add_argument('--datasets', type=str, default="freesolv", help='path to exp folder')
    parser.add_argument('--dir_name', type=str, default="", help='rdkit/seed0，如果构象不是存储在 processed 时使用')
    parser.add_argument('--task_type', type=str, default="classification", help='path to exp folder')
    parser.add_argument('--smiles_column', type=str, default="smiles", help='')
    parser.add_argument('--label_column', type=str, default="label", help='')
    parser.add_argument('--use_processed_csv', action='store_true', default=False, help='')
    parser.add_argument('--graph_feat_extractor', type=str, default="ogb", choices=["ogb", "jure", "geom3d", "unimol", "geom3d_pure_atomic_num", "geom3d_pure_atomic_num", "geom3d_pure_atomic_num_full_edge"], help='')
    args = parser.parse_args()

    datasets = args.datasets.split(",")
    for dataset in datasets:
        if args.use_processed_csv:
            csv_path = f"{args.dataroot}/{dataset}/processed/{dataset}_processed_ac.csv"
        else:
            csv_path = f"{args.dataroot}/{dataset}/raw/{dataset}.csv"

        df = pd.read_csv(csv_path)

        processed_saveroot = f"{args.dataroot}/{dataset}/processed/{args.dir_name}"
        if not os.path.exists(processed_saveroot):
            os.makedirs(processed_saveroot)

        graph_list = []
        for index, smiles, label in tqdm(zip(df["index"].tolist(), df[args.smiles_column].tolist(), df[args.label_column].tolist()), total=len(df["index"].tolist())):
            if isinstance(label, str):
                label = [float(item) for item in label.split(" ")]

            sdf_path = f"{processed_saveroot}/sdfs/{index}.sdf"

            # generate graph
            graph = create_3d_graph_from_sdf(sdf_path, label, index, pre_filter=None, pre_transform=None,
                                             task_type=args.task_type, graph_feat_extractor=args.graph_feat_extractor)
            if graph is None:
                print(f"error in {smiles}")
                raise Exception
            graph_list.append(graph)
        data, slices = InMemoryDataset.collate(graph_list)

        if args.label_column == "label":
            save_path = f"{processed_saveroot}/geometric_3d_data_processed_{args.graph_feat_extractor}_format.pt"
        else:
            save_path = f"{processed_saveroot}/geometric_3d_data_processed_{args.label_column}_{args.graph_feat_extractor}_format.pt"

        print(f"save to {save_path}")
        torch.save((data, slices), save_path)

        # df["smiles"].to_csv(f"{processed_saveroot}/smiles.csv", index=False, header=None)
