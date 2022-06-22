# 4 Dipeptide deviation from expected mean (DDE)
myCodons = {
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2
}
encodings = []
AA = 'ACDEFGHIKLMNPQRSTVWY'
diPeptides = [aa1 + aa2 for aa1 in AA for aa2 in AA]
header = ['#'] + diPeptides
encodings.append(header)

myTM = []
for pair in diPeptides:
    myTM.append((myCodons[pair[0]] / 61) * (myCodons[pair[1]] / 61))

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

    myTV = []
    for j in range(len(myTM)):
        myTV.append(myTM[j] * (1-myTM[j]) / (len(sequence) - 1))

    for j in range(len(tmpCode)):
        tmpCode[j] = (tmpCode[j] - myTM[j]) / math.sqrt(myTV[j])

    code = code + tmpCode
    encodings.append(code)
#saving extracted features
from collections import Counter
import pandas as pd
file = ('DDE.tsv')
with open(file, 'w') as f:
        for i in range(len(encodings[0]) - 1):
            f.write(encodings[0][i] + '\t')
        f.write(encodings[0][-1] + '\n')
        for i in encodings[1:]:
            f.write(i[0] + '\t')
            for j in range(1, len(i) - 1):
                f.write(str(float(i[j])) + '\t')
            f.write(str(float(i[len(i)-1])) + '\n')
tsv_file=('DDE.tsv')
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('DDE.csv',index=False)