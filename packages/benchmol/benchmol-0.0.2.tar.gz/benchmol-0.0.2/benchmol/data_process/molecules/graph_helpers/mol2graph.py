import torch
from torch_geometric.data import Data
from ogb.utils.mol import smiles2graph
from rdkit import Chem
import numpy as np


def mol_to_graph_data_ogb(smiles_str):
    """
    https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py
    using ogb to extract graph features

    :param smiles_str:
    :return:
    """
    graph_dict = smiles2graph(smiles_str)  # introduction of features: https://blog.csdn.net/qq_38862852/article/details/106312171
    edge_attr = torch.tensor(graph_dict["edge_feat"], dtype=torch.long)
    edge_index = torch.tensor(graph_dict["edge_index"], dtype=torch.long)
    x = torch.tensor(graph_dict["node_feat"], dtype=torch.long)
    return x, edge_index, edge_attr


def mol_to_graph_data_jure(smiles):
    # https://github.com/snap-stanford/pretrain-gnns/blob/master/chem/loader.py
    # allowable node and edge features
    allowable_features = {
        'possible_atomic_num_list': list(range(1, 119)),
        'possible_formal_charge_list': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'possible_chirality_list': [
            Chem.rdchem.ChiralType.CHI_UNSPECIFIED,
            Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CW,
            Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CCW,
            Chem.rdchem.ChiralType.CHI_OTHER
        ],
        'possible_hybridization_list': [
            Chem.rdchem.HybridizationType.S,
            Chem.rdchem.HybridizationType.SP, Chem.rdchem.HybridizationType.SP2,
            Chem.rdchem.HybridizationType.SP3, Chem.rdchem.HybridizationType.SP3D,
            Chem.rdchem.HybridizationType.SP3D2, Chem.rdchem.HybridizationType.UNSPECIFIED
        ],
        'possible_numH_list': [0, 1, 2, 3, 4, 5, 6, 7, 8],
        'possible_implicit_valence_list': [0, 1, 2, 3, 4, 5, 6],
        'possible_degree_list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'possible_bonds': [
            Chem.rdchem.BondType.SINGLE,
            Chem.rdchem.BondType.DOUBLE,
            Chem.rdchem.BondType.TRIPLE,
            Chem.rdchem.BondType.AROMATIC
        ],
        'possible_bond_dirs': [  # only for double bond stereo information
            Chem.rdchem.BondDir.NONE,
            Chem.rdchem.BondDir.ENDUPRIGHT,
            Chem.rdchem.BondDir.ENDDOWNRIGHT
        ]
    }

    mol = Chem.MolFromSmiles(smiles)
    # atoms
    num_atom_features = 2   # atom type,  chirality tag
    atom_features_list = []
    for atom in mol.GetAtoms():
        atom_feature = [allowable_features['possible_atomic_num_list'].index(atom.GetAtomicNum())] + [allowable_features['possible_chirality_list'].index(atom.GetChiralTag())]
        atom_features_list.append(atom_feature)
    x = torch.tensor(np.array(atom_features_list), dtype=torch.long)

    # bonds
    num_bond_features = 2   # bond type, bond direction
    if len(mol.GetBonds()) > 0: # mol has bonds
        edges_list = []
        edge_features_list = []
        for bond in mol.GetBonds():
            i = bond.GetBeginAtomIdx()
            j = bond.GetEndAtomIdx()
            if bond.GetBondType() == Chem.rdchem.BondType.DATIVE:  # 配位键通常被视为单键，为了防止报错直接设置为单键
                edge_feature = [allowable_features['possible_bonds'].index(Chem.rdchem.BondType.SINGLE)] + [allowable_features['possible_bond_dirs'].index(bond.GetBondDir())]
            else:
                edge_feature = [allowable_features['possible_bonds'].index(bond.GetBondType())] + [allowable_features['possible_bond_dirs'].index(bond.GetBondDir())]
            edges_list.append((i, j))
            edge_features_list.append(edge_feature)
            edges_list.append((j, i))
            edge_features_list.append(edge_feature)

        # data.edge_index: Graph connectivity in COO format with shape [2, num_edges]
        edge_index = torch.tensor(np.array(edges_list).T, dtype=torch.long)

        # data.edge_attr: Edge feature matrix with shape [num_edges, num_edge_features]
        edge_attr = torch.tensor(np.array(edge_features_list),
                                 dtype=torch.long)
    else:   # mol has no bonds
        edge_index = torch.empty((2, 0), dtype=torch.long)
        edge_attr = torch.empty((0, num_bond_features), dtype=torch.long)

    return x, edge_index, edge_attr


def mol_to_graph_data_graphmvp(smiles):
    # https://github.com/chao1224/GraphMVP/blob/main/src_classification/datasets/molecule_datasets.py
    allowable_features = {
        'possible_atomic_num_list': list(range(1, 119)),
        'possible_formal_charge_list': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'possible_chirality_list': [
            Chem.rdchem.ChiralType.CHI_UNSPECIFIED,
            Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CW,
            Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CCW,
            Chem.rdchem.ChiralType.CHI_OTHER
        ],
        'possible_hybridization_list': [
            Chem.rdchem.HybridizationType.S,
            Chem.rdchem.HybridizationType.SP,
            Chem.rdchem.HybridizationType.SP2,
            Chem.rdchem.HybridizationType.SP3,
            Chem.rdchem.HybridizationType.SP3D,
            Chem.rdchem.HybridizationType.SP3D2,
            Chem.rdchem.HybridizationType.UNSPECIFIED
        ],
        'possible_numH_list': [0, 1, 2, 3, 4, 5, 6, 7, 8],
        'possible_implicit_valence_list': [0, 1, 2, 3, 4, 5, 6],
        'possible_degree_list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'possible_bonds': [
            Chem.rdchem.BondType.SINGLE,
            Chem.rdchem.BondType.DOUBLE,
            Chem.rdchem.BondType.TRIPLE,
            Chem.rdchem.BondType.AROMATIC
        ],
        'possible_bond_dirs': [  # only for double bond stereo information
            Chem.rdchem.BondDir.NONE,
            Chem.rdchem.BondDir.ENDUPRIGHT,
            Chem.rdchem.BondDir.ENDDOWNRIGHT
        ]
    }

    mol = Chem.MolFromSmiles(smiles)
    # atoms
    # num_atom_features = 2  # atom type, chirality tag
    atom_features_list = []
    for atom in mol.GetAtoms():
        atom_feature = [allowable_features['possible_atomic_num_list'].index(atom.GetAtomicNum())] + \
                       [allowable_features['possible_chirality_list'].index(atom.GetChiralTag())]
        atom_features_list.append(atom_feature)
    x = torch.tensor(np.array(atom_features_list), dtype=torch.long)

    # bonds
    if len(mol.GetBonds()) <= 0:  # mol has no bonds
        num_bond_features = 2  # bond type & direction
        edge_index = torch.empty((2, 0), dtype=torch.long)
        edge_attr = torch.empty((0, num_bond_features), dtype=torch.long)
    else:  # mol has bonds
        edges_list = []
        edge_features_list = []
        for bond in mol.GetBonds():
            i = bond.GetBeginAtomIdx()
            j = bond.GetEndAtomIdx()
            edge_feature = [allowable_features['possible_bonds'].index(bond.GetBondType())] + \
                           [allowable_features['possible_bond_dirs'].index(bond.GetBondDir())]
            edges_list.append((i, j))
            edge_features_list.append(edge_feature)
            edges_list.append((j, i))
            edge_features_list.append(edge_feature)

        # data.edge_index: Graph connectivity in COO format with shape [2, num_edges]
        edge_index = torch.tensor(np.array(edges_list).T, dtype=torch.long)

        # data.edge_attr: Edge feature matrix with shape [num_edges, num_edge_features]
        edge_attr = torch.tensor(np.array(edge_features_list), dtype=torch.long)

    return x, edge_index, edge_attr


def mol_to_graph_data_molclr(smiles):
    # https://github.com/yuyangw/MolCLR/blob/master/dataset/dataset.py
    ATOM_LIST = list(range(1, 119))
    CHIRALITY_LIST = [
        Chem.rdchem.ChiralType.CHI_UNSPECIFIED,
        Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CW,
        Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CCW,
        Chem.rdchem.ChiralType.CHI_OTHER
    ]
    BOND_LIST = [
        Chem.rdchem.BondType.SINGLE,
        Chem.rdchem.BondType.DOUBLE,
        Chem.rdchem.BondType.TRIPLE,
        Chem.rdchem.BondType.AROMATIC
    ]
    BONDDIR_LIST = [
        Chem.rdchem.BondDir.NONE,
        Chem.rdchem.BondDir.ENDUPRIGHT,
        Chem.rdchem.BondDir.ENDDOWNRIGHT
    ]

    mol = Chem.MolFromSmiles(smiles)

    type_idx = []
    chirality_idx = []
    atomic_number = []
    for atom in mol.GetAtoms():
        type_idx.append(ATOM_LIST.index(atom.GetAtomicNum()))
        chirality_idx.append(CHIRALITY_LIST.index(atom.GetChiralTag()))
        atomic_number.append(atom.GetAtomicNum())

    x1 = torch.tensor(type_idx, dtype=torch.long).view(-1, 1)
    x2 = torch.tensor(chirality_idx, dtype=torch.long).view(-1, 1)
    x = torch.cat([x1, x2], dim=-1)

    row, col, edge_feat = [], [], []
    for bond in mol.GetBonds():
        start, end = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        row += [start, end]
        col += [end, start]
        edge_feat.append([
            BOND_LIST.index(bond.GetBondType()),
            BONDDIR_LIST.index(bond.GetBondDir())
        ])
        edge_feat.append([
            BOND_LIST.index(bond.GetBondType()),
            BONDDIR_LIST.index(bond.GetBondDir())
        ])

    edge_index = torch.tensor([row, col], dtype=torch.long)
    edge_attr = torch.tensor(np.array(edge_feat), dtype=torch.long)

    return x, edge_index, edge_attr


def create_graph_from_smiles(smiles, label, index=None, pre_filter=None, pre_transform=None, task_type="classification", graph_feat_extractor="ogb"):
    assert task_type in ["classification", "regression"]
    assert graph_feat_extractor in ["ogb", "jure", "molclr", "graphmvp"]

    try:
        if graph_feat_extractor == "ogb":
            x, edge_index, edge_attr = mol_to_graph_data_ogb(smiles)
        elif graph_feat_extractor == "jure":
            x, edge_index, edge_attr = mol_to_graph_data_jure(smiles)
        elif graph_feat_extractor == "molclr":
            x, edge_index, edge_attr = mol_to_graph_data_molclr(smiles)
        elif graph_feat_extractor == "graphmvp":
            x, edge_index, edge_attr = mol_to_graph_data_graphmvp(smiles)
        else:
            raise Exception("graph_feat_extractor {} is undefined".format(graph_feat_extractor))

        if task_type == "classification":
            y = torch.tensor(label, dtype=torch.long).view(1, -1)
        else:
            y = torch.tensor(label, dtype=torch.float).view(1, -1)
        graph = Data(edge_attr=edge_attr, edge_index=edge_index, x=x, y=y, index=index)
        if pre_filter is not None and pre_filter(graph):
            return None
        if pre_transform is not None:
            graph = pre_transform(graph)
        return graph
    except:
        return None


if __name__ == '__main__':
    smiles = "C1C[N+]23CCC[N+]4(C1)CC[S-]1[Fe+2]24([SH+]CC3)[S-]2CC[N+]34CCC[N+]5(CCC3)CC[SH+][Fe+2]1254"
    graph1 = create_graph_from_smiles(smiles, label=-1, graph_feat_extractor="ogb")
    graph2 = create_graph_from_smiles(smiles, label=-1, graph_feat_extractor="jure")
    graph3 = create_graph_from_smiles(smiles, label=-1, graph_feat_extractor="molclr")
    graph4 = create_graph_from_smiles(smiles, label=-1, graph_feat_extractor="graphmvp")

    # jure, molclr, graphmvp 用的 graph 是完全一样的。因此，使用 jure 的就可以了。
    assert (graph2.x == graph3.x).all() and (graph2.x == graph4.x).all()
    assert (graph2.edge_index == graph3.edge_index).all() and (graph2.edge_index == graph4.edge_index).all()
    assert (graph2.edge_attr == graph3.edge_attr).all() and (graph2.edge_attr == graph4.edge_attr).all()

    print(graph1)