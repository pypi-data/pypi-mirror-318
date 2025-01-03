import os.path
from argparse import ArgumentParser

import numpy as np
import pandas as pd
from rdkit import Chem
from sklearn.impute import SimpleImputer
from tqdm import tqdm

from benchmol.data_process.molecules.fingerprints import fpFunc_dict


def get_fp_names():
    return list(fpFunc_dict.keys())


class FeaturesGeneration:
    def __init__(self):
        self.fingerprints = []

    def get_fingerprints_from_smiles_list(self, smiles_list, fp_name):
        df = pd.DataFrame({
            "smiles": smiles_list,
        })
        return self.get_fingerprints(df, fp_name, smiles_column_name="smiles")

    def get_fingerprints(self, df, fp_name, smiles_column_name="SMILES"):
        smiles_list = df[smiles_column_name].to_list()
        not_found = []

        # if fp_name == "tpatf":
        #     pool = Pool(10)
        #     res = pool.map(fpFunc_dict[fp_name], smiles_list)
        #     print(res)
        # else:
        for smi in tqdm(smiles_list, total=len(smiles_list)):
            try:
                m = Chem.MolFromSmiles(smi)
                fp = fpFunc_dict[fp_name](m)
                bit_array = np.asarray(fp)
                self.fingerprints.append(bit_array)
            except:
                not_found.append(smi)
                if fp_name == 'tpatf':
                    add = [np.nan for _ in range(self.fingerprints[0].shape[1])]
                elif fp_name == 'rdkDes':
                    add = [np.nan for _ in range(len(self.fingerprints[0]))]
                else:
                    add = [np.nan for _ in range(len(self.fingerprints[0]))]
                tpatf_arr = np.array(add, dtype=np.float32)
                self.fingerprints.append(tpatf_arr)

        if fp_name == 'rdkDes':
            X = np.array(self.fingerprints)
            ndf = pd.DataFrame.from_records(X)
            r, _ = np.where(df.isna())

            for col in ndf.columns:
                ndf[col].fillna(ndf[col].mean(), inplace=True)  # nan 用 均值填充

            X = ndf.iloc[:, 0:].values
            X = X.astype(np.float32)
            X = np.nan_to_num(X)
        else:
            fp_array = (np.asarray((self.fingerprints), dtype=object))
            X = np.vstack(fp_array).astype(np.float32)
            imp_median = SimpleImputer(missing_values=np.nan, strategy='median')
            imp_median.fit(X)
            X = imp_median.transform(X)

        final_array = X
        self.fingerprints = []
        return final_array

