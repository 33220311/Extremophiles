# 3- Dipeptide composition(DC)
encodings = []
diPeptides = [aa1 + aa2 for aa1 in AA for aa2 in AA]
header = ['#'] + diPeptides
encodings.append(header)

AADict = {}
for i in range(len(AA)):
        AADict[AA[i]] = i

for i in myFasta:
        name, sequence = i[0], re.sub('-', '', i[1])
        code = [name]
        tmpCode = [0] * 400
        for j in range(len(sequence) - 2 + 1):
            tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[j+1]]] = tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[j+1]]] +1
        if sum(tmpCode) != 0:
            tmpCode = [i/sum(tmpCode) for i in tmpCode]
        code = code + tmpCode
        encodings.append(code)
#saving extracted features
from collections import Counter
import pandas as pd
file = ('DPC.tsv')
with open(file, 'w') as f:
        for i in range(len(encodings[0]) - 1):
            f.write(encodings[0][i] + '\t')
        f.write(encodings[0][-1] + '\n')
        for i in encodings[1:]:
            f.write(i[0] + '\t')
            for j in range(1, len(i) - 1):
                f.write(str(float(i[j])) + '\t')
            f.write(str(float(i[len(i)-1])) + '\n')
tsv_file=('DPC.tsv')
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('DPC.csv',index=False)