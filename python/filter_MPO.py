from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors as rdescriptors
import pandas as pd

def lipinski_wt_limit(m):
    if Descriptors.MolWt(m) <= 360:
        m,num = m,1
    else:
        m,num = 0,0
    return m,num

def lipinski_logp_limit(m):
    if Descriptors.MolLogP(m) <= 3:
        m,num = m,1
    else:
        m,num = 0,0
    return m,num

   
def lipinski_hba_limit(m):
    if rdescriptors.CalcNumLipinskiHBA(m) <= 10:
        m,num = m,1
    else:
        m,num = 0,0
    return m,num
    

def lipinski_hbd_limit(m):
    if rdescriptors.CalcNumLipinskiHBD(m) <= 0:
        m,num = m,1
    else:
        m,num = 0,0
    return m,num
    

data = pd.read_csv('./demo.smi', delimiter=' ',header = None)
#print(data)
smile_dic = {}
for i in range(len(data)):
    temp_smile = data.iloc[i,0]
    temp_name = data.iloc[i,1]
    #print(temp_smile)
    m = Chem.MolFromSmiles(temp_smile)
    m_w,num_w = lipinski_wt_limit(m)
    m_l,num_l = lipinski_logp_limit(m)
    m_a,num_a = lipinski_hba_limit(m)
    m_d,num_d = lipinski_hbd_limit(m)    
    if m_w and m_l and m_a and m_d: 
        smile_dic[temp_smile]=temp_name
#print(smile_dic)
out_path = './demo_MPO.csv'
df = pd.Series(smile_dic).T
df.to_csv(out_path)        