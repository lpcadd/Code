#!/home/li_peng/03_install/anaconda3/envs/my-rdkit-env/bin/python3.7
# python sdftosmiles.py molecules.sdf
import sys
from rdkit import Chem
def converter(file_name):
    mols = [ mol for mol in Chem.SDMolSupplier( file_name ) ]
    outname = file_name.split(".sdf")[0] + ".smi"
    out_file = open( outname, "w" )
    for mol in mols:
        smi = Chem.MolToSmiles(mol)
        name = mol.GetProp("_Name")
        out_file.write( "{}\t{}\n".format(smi, name ))
    out_file.close()
if __name__=="__main__":
    converter( sys.argv[1] )

