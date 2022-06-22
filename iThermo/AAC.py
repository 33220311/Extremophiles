# 1-Amino acid composition(AAC)
AA = 'ACDEFGHIKLMNPQRSTVWY'
encodings = []
header = ['#']
for i in AA:
    header.append(i)
encodings.append(header)
for i in myFasta:
    name, sequence = i[0], re.sub('-', '', i[1])
    count = Counter(sequence)
    for key in count:
        count[key] = count[key]/len(sequence)
    code = [name]
    for aa in AA:
        code.append(count[aa])
    encodings.append(code)
#saving extracted features
from collections import Counter
import pandas as pd
file = ('AAC.tsv')
with open(file, 'w') as f:
        for i in range(len(encodings[0]) - 1):
            f.write(encodings[0][i] + '\t')
        f.write(encodings[0][-1] + '\n')
        for i in encodings[1:]:
            f.write(i[0] + '\t')
            for j in range(1, len(i) - 1):
                f.write(str(float(i[j])) + '\t')
            f.write(str(float(i[len(i)-1])) + '\n')
tsv_file=('AAC.tsv')
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('AAC.csv',index=False)