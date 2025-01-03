#######################################################################
# Author: Srijan Verma                                                #
# Department of Pharmacy                                              #
# Birla Institute of Technology and Science, Pilani, India            #
# Last modified: 13/08/2020                                           #
#######################################################################

import os
import shutil
import tempfile

import numpy as np
from rdkit import Chem
from rdkit.Avalon import pyAvalonTools as fpAvalon
from rdkit.Chem import AllChem, Descriptors
from rdkit.Chem import MACCSkeys
from rdkit.Chem import rdMolDescriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit import DataStructs

# RDKit descriptors -->
calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])


# Function for generating TPATF features, using Mayachem tools
def get_tpatf(m):

    # Creates a temp folder
    temp_dir = tempfile.mkdtemp()

    # Compute 2D coordinates
    AllChem.Compute2DCoords(m)

    # Save sdf file
    w = Chem.SDWriter(os.path.join(temp_dir, "temp.sdf"))
    w.write(m)
    w.flush()

    try:
        # Path to perl script
        script_path = '../mayachemtools/bin/TopologicalPharmacophoreAtomTripletsFingerprints.pl'
        command = "perl " + script_path + " -r " + os.path.join(temp_dir, "temp") + " --AtomTripletsSetSizeToUse FixedSize -v ValuesString -o " + os.path.join(temp_dir, "temp.sdf")
        os.system(command)

        with open(os.path.join(temp_dir, "temp.csv"), 'r') as f:
            for line in f.readlines():
                if "Cmpd" in line:
                    line = line.split(';')[5].replace('"', '')
                    features = [int(i) for i in line.split(" ")]
    except:
        features = None

    # Delete the temporary directory
    shutil.rmtree(temp_dir)

    tpatf_arr = np.array(features, dtype=np.float32)
    tpatf_arr = tpatf_arr.reshape(1, tpatf_arr.shape[0])
    return tpatf_arr


def physchem(mol):
    # Reference: https://github.com/dengjianyuan/Respite_MPP/blob/9f3df9e2af747091edb6d60bb06b56294ce24dc4/src/dataset.py#L47
    weight = Descriptors.ExactMolWt(mol)
    logp = Descriptors.MolLogP(mol)
    h_bond_donor = Descriptors.NumHDonors(mol)
    h_bond_acceptors = Descriptors.NumHAcceptors(mol)
    rotatable_bonds = Descriptors.NumRotatableBonds(mol)
    atoms = Chem.rdchem.Mol.GetNumAtoms(mol)
    heavy_atoms = Chem.rdchem.Mol.GetNumHeavyAtoms(mol)
    molar_refractivity = Chem.Crippen.MolMR(mol)
    topological_polar_surface_area = Chem.QED.properties(mol).PSA
    formal_charge = Chem.rdmolops.GetFormalCharge(mol)
    rings = Chem.rdMolDescriptors.CalcNumRings(mol)
    # form features matrix
    features = np.array(
        [weight, logp, h_bond_donor, h_bond_acceptors, rotatable_bonds, atoms, heavy_atoms, molar_refractivity,
         topological_polar_surface_area, formal_charge, rings])

    return features


def MCFP(m, radius, nBits):
    """Reference: https://github.com/dengjianyuan/Respite_MPP/blob/9f3df9e2af747091edb6d60bb06b56294ce24dc4/src/dataset.py#L45
    """
    features_vec = AllChem.GetHashedMorganFingerprint(m, radius=radius, nBits=nBits)
    features = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(features_vec, features)
    return features

def atompair(m, nBits, use2D):
    features_vec = rdMolDescriptors.GetHashedAtomPairFingerprint(m, nBits=nBits, use2D=use2D)
    features = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(features_vec, features)
    return features


longbits = 16384

# dictionary
fpFunc_dict = {}
for nbits in [1024, 2048]:  # common value is 1024 and 2048
    fpFunc_dict[f'ecfp0_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 0, nBits=nbits)
    fpFunc_dict[f'ecfp2_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 1, nBits=nbits)
    fpFunc_dict[f'ecfp4_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=nbits)
    fpFunc_dict[f'ecfp6_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 3, nBits=nbits)
    fpFunc_dict[f'mcfp0_{nbits}'] = lambda m: MCFP(m, radius=0, nBits=nbits)  # MorganCounts fingerprints。ECFP 出现次数可以保留下来，这与 MorganCounts 指纹相对应。
    fpFunc_dict[f'mcfp2_{nbits}'] = lambda m: MCFP(m, radius=1, nBits=nbits)  # MorganCounts fingerprints。ECFP 出现次数可以保留下来，这与 MorganCounts 指纹相对应。
    fpFunc_dict[f'mcfp4_{nbits}'] = lambda m: MCFP(m, radius=2, nBits=nbits)  # MorganCounts fingerprints。ECFP 出现次数可以保留下来，这与 MorganCounts 指纹相对应。
    fpFunc_dict[f'mcfp6_{nbits}'] = lambda m: MCFP(m, radius=3, nBits=nbits)  # MorganCounts fingerprints。ECFP 出现次数可以保留下来，这与 MorganCounts 指纹相对应。
    fpFunc_dict[f'fcfp2_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 1, useFeatures=True, nBits=nbits)
    fpFunc_dict[f'fcfp4_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 2, useFeatures=True, nBits=nbits)
    fpFunc_dict[f'fcfp6_{nbits}'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 3, useFeatures=True, nBits=nbits)
    fpFunc_dict[f'hashap_{nbits}'] = lambda m: rdMolDescriptors.GetHashedAtomPairFingerprintAsBitVect(m, nBits=nbits)
    fpFunc_dict[f'hashtt_{nbits}'] = lambda m: rdMolDescriptors.GetHashedTopologicalTorsionFingerprintAsBitVect(m, nBits=nbits)
    fpFunc_dict[f'avalon_{nbits}'] = lambda m: fpAvalon.GetAvalonFP(m, nbits)
    fpFunc_dict[f'rdk5_{nbits}'] = lambda m: Chem.RDKFingerprint(m, maxPath=5, fpSize=nbits, nBitsPerHash=2)
    fpFunc_dict[f'rdk6_{nbits}'] = lambda m: Chem.RDKFingerprint(m, maxPath=6, fpSize=nbits, nBitsPerHash=2)
    fpFunc_dict[f'rdk7_{nbits}'] = lambda m: Chem.RDKFingerprint(m, maxPath=7, fpSize=nbits, nBitsPerHash=2)
    fpFunc_dict[f'atompair_{nbits}'] = lambda m: atompair(m, nBits=nbits, use2D=True)  # atomPairs: https://github.com/dengjianyuan/Respite_MPP/blob/9f3df9e2af747091edb6d60bb06b56294ce24dc4/src/dataset.py#L47

fpFunc_dict['lecfp4'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=longbits)
fpFunc_dict['lecfp6'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 3, nBits=longbits)
fpFunc_dict['lfcfp4'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 2, useFeatures=True, nBits=longbits)
fpFunc_dict['lfcfp6'] = lambda m: AllChem.GetMorganFingerprintAsBitVect(m, 3, useFeatures=True, nBits=longbits)
fpFunc_dict['maccs'] = lambda m: MACCSkeys.GenMACCSKeys(m)
fpFunc_dict['laval'] = lambda m: fpAvalon.GetAvalonFP(m, longbits)
fpFunc_dict['rdkDes'] = lambda m: calc.CalcDescriptors(m)
fpFunc_dict['tpatf'] = lambda m: get_tpatf(m)

fpFunc_dict['physchem'] = lambda m: physchem(m)



