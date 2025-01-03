from rdkit import Chem
from rdkit.Chem import Draw


def loadSmilesAndSave(smis, path):
    '''
        smis: e.g. COC1=C(C=CC(=C1)NS(=O)(=O)C)C2=CN=CN3C2=CC=C3
        path: E:/a/b/c.png

        ==============================================================================================================
        demo:
            smiless = ["OC[C@@H](NC(=O)C(Cl)Cl)[C@H](O)C1=CC=C(C=C1)[N+]([O-])=O", "CN1CCN(CC1)C(C1=CC=CC=C1)C1=CC=C(Cl)C=C1",
              "[H][C@@](O)(CO)[C@@]([H])(O)[C@]([H])(O)[C@@]([H])(O)C=O", "CNC(NCCSCC1=CC=C(CN(C)C)O1)=C[N+]([O-])=O",
              "[H]C(=O)[C@H](O)[C@@H](O)[C@@H](O)[C@H](O)CO", "CC[C@H](C)[C@H](NC(=O)[C@H](CC1=CC=C(O)C=C1)NC(=O)[C@@H](NC(=O)[C@H](CCCN=C(N)N)NC(=O)[C@@H](N)CC(O)=O)C(C)C)C(=O)N[C@@H](CC1=CN=CN1)C(=O)N1CCC[C@H]1C(=O)N[C@@H](CC1=CC=CC=C1)C(O)=O"]

            for idx, smiles in enumerate(smiless):
                loadSmilesAndSave(smiles, "{}.png".format(idx+1))
        ==============================================================================================================

    '''
    mol = Chem.MolFromSmiles(smis)
    img = Draw.MolsToGridImage([mol], molsPerRow=1, subImgSize=(224, 224))
    img.save(path)

