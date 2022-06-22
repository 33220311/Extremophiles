#feature selection
aac =pd.read_csv('AAC.csv')[['A', 'Q', 'I', 'K', 'T', 'E','S','Y', 'V','D']]
paac = pd.read_csv('PAAC.csv')[['Xc1.A','Xc1.E','Xc1.T','Xc1.D', 'Xc1.S', 'Xc1.Q','Xc1.G', 'Xc1.K']]
apaac = pd.read_csv('APAAC.csv')[['Pc1.A', 'Pc1.Q','Pc1.K', 'Pc1.G', 'Pc1.S', 'Pc1.E', 'Pc1.T', 'Pc1.I']]
dpc = pd.read_csv('DPC.csv')[['AA','EE', 'KE', 'EK', 'KK', 'LK', 'EI', 'KI','IK', 'LA']]
dpde = pd.read_csv('DDE.csv')[['ke','aa', 'ee']] 
cksaap = pd.read_csv('CKSAAP.csv')[['EK.gap2', 'EK.gap3','AA.gap2', 'AA.gap1']] 
ctdc=pd.read_csv('CTDC.csv').drop(labels=['#'], axis=1)
#feature fusion
cf1 =pd.merge(paac.reset_index(),apaac.reset_index(),how='inner').drop(labels=['index'], axis=1)
cf2 =pd.merge(cf1.reset_index(), ctdc.reset_index(), how='inner').drop(labels=['index'], axis=1)
cf3 =pd.merge(cf2.reset_index(), cksaap.reset_index(), how='inner').drop(labels=['index'], axis=1)
cf4 =pd.merge(cf3.reset_index(), dpde.reset_index(), how='inner').drop(labels=['index'], axis=1)
cf5 =pd.merge(cf4.reset_index(), aac.reset_index(), how='inner').drop(labels=['index'], axis=1)
cf6 =pd.merge(cf5.reset_index(), dpc.reset_index(), how='inner').drop(labels=['index'], axis=1)
# adding label
cf7 =pd.merge(pd.read_csv('label.csv').reset_index(), cf6.reset_index(), how='inner').drop(labels=['index'], axis=1)