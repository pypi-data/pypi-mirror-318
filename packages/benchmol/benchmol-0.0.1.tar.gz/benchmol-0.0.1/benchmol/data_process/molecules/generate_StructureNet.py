import os
import warnings

import numpy as np
import pandas as pd
from pandas.errors import SettingWithCopyWarning

from utils.splitter import scaffold_split_train_val_test, split_train_val_test_idx, \
    random_scaffold_split_train_val_test, scaffold_split_balanced_train_val_test

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

"""
包括 6 种分子类型：
1. 网状分子
2. 无环分子
3. 完全链式分子
4. 无环链式分子
5. 大环肽（带有肽键，不一定是肽）
6. 大分子

构建过程如下，以网状分子为例：
1. 按照条件筛选出网状分子；
2. 根据靶点（Assay ChEMBL ID）和标签类型（Standard Type）进行 group；
3. 选择数量最多的 n 个 group 来构建数据集。这里需要特别注意单位
"""


class StructureNet:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)
        assert len(self.df["Standard Relation"].unique()) == 1 and self.df["Standard Relation"].unique()[0] == "'='"  # 单位必须是等于符号
        self.all_columns = ['index', 'Molecule ChEMBL ID', 'smiles', 'canonical_smiles', "scaffold", 'Standard Type', 'Standard Relation', 'Standard Value', 'Standard Units', 'Assay ChEMBL ID', 'Target ChEMBL ID', 'num_ring', 'average_degree', 'has_branch', 'max_ring', 'num_amide', 'MW']
        self.grouped_columns = ['Assay ChEMBL ID', 'Standard Type', 'Standard Units']

    def generate_data(self, df, n_top_targets, splitter, save_dir):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 在按照 ('Target ChEMBL ID', 'Standard Type', 'Standard Units') 分组后，按照组内的数据量（对 smiles 去重再统计）从大到小排序
        tmp = [(len(item[1]["smiles"].unique()), item) for item in list(df.groupby(by=self.grouped_columns, dropna=True))]
        grouped_df = sorted(tmp, key=lambda x: (x[0], x[1]), reverse=True)
        # print(f"grouped_df: {len(grouped_df)}")
        index = 0
        for total_unique, (grouped_data, part_df) in grouped_df:
            target_ID, standard_type, standard_units = grouped_data[0], grouped_data[1], grouped_data[2]
            standard_type = standard_type.replace(" ", "_")  # Percent Effect 有空格，使用 _ 连接它
            filename = f"{target_ID}_{standard_type}_{standard_units}"
            # part_df 中存在重复的 smiles，标签使用均值来替代
            part_df = self.drop_duplicate_smiles_use_mean(part_df)  # 按照 assay 计算均值
            if standard_units == "nM":
                part_df["label"] = -np.log10(part_df["Standard Value"])  # pValue, 参考：https://arxiv.org/pdf/2201.09637
                print(f"[{filename}] [label=-log10(Standard Value)] min: {part_df.label.min()}; max: {part_df.label.max()}")
            else:
                part_df["label"] = part_df["Standard Value"]
                print(f"[{filename}] [label=Standard Value] min: {part_df.label.min()}; max: {part_df.label.max()}")
            if len(part_df) <= 300:
                frac_train, frac_valid, frac_test = 0.6, 0.2, 0.2
            else:
                frac_train, frac_valid, frac_test = 0.8, 0.1, 0.1
            self.add_scaffold_split_column(part_df, splitter=splitter, desc=filename, frac_train=frac_train, frac_valid=frac_valid, frac_test=frac_test)
            # print(f"save to {save_dir}/{filename}.csv)
            part_df.to_csv(f"{save_dir}/{filename}.csv", index=False)
            assert total_unique == part_df.shape[0]  # smiles 必须唯一

            index += 1
            if index == n_top_targets:
                break
            print("")

    def drop_duplicate_smiles_use_mean(self, df, mean_columns="Standard Value"):
        """使用 smiles 分组后，mean_columns 替换为均值，其它的列使用重复的第一条数据"""
        grouped_df_list = []
        for smiles, grouped_df in df.groupby("smiles"):
            if len(grouped_df) == 1:
                grouped_df_list.append(grouped_df)
            else:
                first_df = grouped_df.head(1)
                first_df[mean_columns] = grouped_df[mean_columns].mean()
                first_df["Assay ChEMBL ID"] = ";".join(grouped_df["Assay ChEMBL ID"].tolist())  # 多个 assay 上结果的均值
                grouped_df_list.append(first_df)
        return pd.concat(grouped_df_list).reset_index(drop=True)

    def add_scaffold_split_column(self, df, splitter="scaffold", seed=42, desc="", frac_train=0.8, frac_valid=0.1, frac_test=0.1):
        assert splitter in ["random", "scaffold", "random_scaffold", "balanced_scaffold"]
        smiles_list = df["smiles"].values.tolist()
        index_list = list(range(len(smiles_list)))

        if splitter == "random":
            train_index, val_index, test_index = split_train_val_test_idx(index_list, frac_train=frac_train, frac_valid=frac_valid,
                                                                          frac_test=frac_test, seed=seed)
        elif splitter == "scaffold":
            train_index, val_index, test_index = scaffold_split_train_val_test(index_list, smiles_list,
                                                                               frac_train=frac_train,
                                                                               frac_valid=frac_valid,
                                                                               frac_test=frac_test)
        elif splitter == "random_scaffold":
            train_index, val_index, test_index = random_scaffold_split_train_val_test(index_list, smiles_list,
                                                                                      frac_train=frac_train,
                                                                                      frac_valid=frac_valid,
                                                                                      frac_test=frac_test, seed=seed)
        elif splitter == "balanced_scaffold":
            train_index, val_index, test_index = scaffold_split_balanced_train_val_test(index_list, smiles_list,
                                                                                        frac_train=frac_train,
                                                                                        frac_valid=frac_valid,
                                                                                        frac_test=frac_test, seed=seed,
                                                                                        balanced=True)
        else:
            raise NotImplementedError

        df[f"{splitter}_split"] = 0
        df.loc[train_index, f"{splitter}_split"] = "train"
        df.loc[val_index, f"{splitter}_split"] = "valid"
        df.loc[test_index, f"{splitter}_split"] = "test"
        print(f"[{desc}] {splitter}_split: {frac_train} train; {frac_valid} valid; {frac_test} test] train: {len(train_index)}, valid: {len(val_index)}, test: {len(test_index)}")

    def reticular_molecules(self, average_degree=2.4, n_top_targets=10, save_dir="./StructureNet/reticular_molecules", splitter="scaffold"):
        """1. 网状分子"""
        df1 = self.df[self.df['average_degree'] > average_degree]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)

    def acyclic_molecules(self, n_top_targets=10, save_dir="./StructureNet/acyclic_molecules", splitter="random"):
        """2. 无环分子
        注意：不支持 scaffold split，因为所有无环分子的 scaffold 为 ''，没法分割
        """
        df1 = self.df[self.df['num_ring'] == 0]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)

    def complete_chain_molecules(self, has_branch=0.2, n_top_targets=10, save_dir="./StructureNet/cyclic_chain_molecules", splitter="scaffold"):
        """3. 完全链式分子
        """
        df1 = self.df[self.df['has_branch'] < has_branch]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)

    def acyclic_chain_molecules(self, has_branch=0.1, num_ring=0, n_top_targets=10, save_dir="./StructureNet/acyclic_chain_molecules", splitter="random"):
        """4. 无环链式分子
            - has_branch: 越小越属于链式分子
            注意：不支持 scaffold split，因为所有无环分子的 scaffold 为 ''，没法分割
        """
        df1 = self.df[(self.df['has_branch'] < has_branch) & (self.df['num_ring'] == num_ring)]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)

    def macrocyclic_peptide_molecules(self, max_ring=12, n_top_targets=10, save_dir="./StructureNet/macrocyclic_peptide_molecules", splitter="scaffold"):
        """5. 大环肽"""
        df1 = self.df[(self.df['max_ring'] > max_ring) & (self.df['num_amide'] > 0)]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)

    def macro_molecules(self, MW=900, n_top_targets=10, save_dir="./StructureNet/macro_molecules", splitter="scaffold"):
        """6. 大分子"""
        df1 = self.df[self.df['MW'] > MW]
        df1.reset_index(drop=True, inplace=True)
        self.generate_data(df1, n_top_targets, splitter, save_dir)


if __name__ == '__main__':
    csv_path = "../../datasets/molecule_types/all.csv"
    structureNet = StructureNet(csv_path)

    n_top_targets = 10
    data_settings = {
        "1. generating reticular_molecules": {
            "type": "reticular_molecules",
            "average_degree": 2.33,
            "save_dir": "../../datasets/molecule_types/StructureNet/reticular_molecules",
            "splitter": "scaffold"
        },
        "2. generating acyclic_molecules": {
            "type": "acyclic_molecules",
            "save_dir": "../../datasets/molecule_types/StructureNet/acyclic_molecules",
            "splitter": "random"
        },
        "3. generating complete_chain_molecules": {
            "type": "complete_chain_molecules",
            "has_branch": 0.2,
            "save_dir": "../../datasets/molecule_types/StructureNet/complete_chain_molecules",
            "splitter": "scaffold"
        },
        "4. generating acyclic_chain_molecules": {
            "type": "acyclic_chain_molecules",
            "has_branch": 0.255,
            "num_ring": 0,
            "save_dir": "../../datasets/molecule_types/StructureNet/acyclic_chain_molecules",
            "splitter": "random"
        },
        "5. generating macrocyclic_peptide_molecules": {
            "type": "macrocyclic_peptide_molecules",
            "max_ring": 12,
            "save_dir": "../../datasets/molecule_types/StructureNet/macrocyclic_peptide_molecules",
            "splitter": "scaffold"
        },
        "6. generating macro_molecules": {
            "type": "macro_molecules",
            "MW": 900,
            "save_dir": "../../datasets/molecule_types/StructureNet/macro_molecules",
            "splitter": "scaffold"
        },
    }

    for key in data_settings.keys():
        data_dict = data_settings[key]
        type = data_dict["type"]
        save_dir = data_dict["save_dir"]
        splitter = data_dict["splitter"]

        if type == "reticular_molecules":  # 网状分子
            print(f"=========== {key} with average_degree={data_dict['average_degree']} ===========")
            structureNet.reticular_molecules(average_degree=data_dict["average_degree"], n_top_targets=n_top_targets, save_dir=save_dir, splitter=splitter)

        elif type == "acyclic_molecules":  # 无环分子
            print(f"=========== {key} ===========")
            structureNet.acyclic_molecules(n_top_targets=10, save_dir=save_dir, splitter=splitter)

        elif type == "complete_chain_molecules":  # 完全链式分子
            print(f"=========== {key} with has_branch={data_dict['has_branch']} ===========")
            structureNet.complete_chain_molecules(has_branch=data_dict["has_branch"], n_top_targets=n_top_targets, save_dir=save_dir, splitter=splitter)

        elif type == "acyclic_chain_molecules":  # 无环链式分子
            print(f"=========== {key} with has_branch={data_dict['has_branch']} and num_ring={data_dict['num_ring']} ===========")
            structureNet.acyclic_chain_molecules(has_branch=data_dict["has_branch"], num_ring=data_dict['num_ring'], n_top_targets=n_top_targets, save_dir=save_dir, splitter=splitter)

        elif type == "macrocyclic_peptide_molecules":  #
            print(f"=========== {key} with max_ring={data_dict['max_ring']} ===========")
            structureNet.macrocyclic_peptide_molecules(max_ring=data_dict["max_ring"], n_top_targets=n_top_targets, save_dir=save_dir, splitter=splitter)

        elif type == "macro_molecules":  # 大分子
            print(f"=========== {key} with MW={data_dict['MW']} ===========")
            structureNet.macro_molecules(MW=data_dict["MW"], n_top_targets=n_top_targets, save_dir=save_dir, splitter=splitter)
        else:
            raise NotImplementedError
        print()