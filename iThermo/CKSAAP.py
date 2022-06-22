# 5 CKSAAP
def CKSAAP(myFasta, gap=5, **kw):
    AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
    encodings = []
    aaPairs = []
    for aa1 in AA:
        for aa2 in AA:
            aaPairs.append(aa1 + aa2)
    header = ['#']
    for g in range(gap+1):
        for aa in aaPairs:
            header.append(aa + '.gap' + str(g))
    encodings.append(header)
    for i in myFasta:
        name, sequence = i[0], i[1]
        code = [name]
        for g in range(gap+1):
            myDict = {}
            for pair in aaPairs:
                myDict[pair] = 0
            sum = 0
            for index1 in range(len(sequence)):
                index2 = index1 + g + 1
                if index1 < len(sequence) and index2 < len(sequence) and sequence[index1] in AA and sequence[index2] in AA:
                    myDict[sequence[index1] + sequence[index2]] = myDict[sequence[index1] + sequence[index2]] + 1
                    sum = sum + 1
            for pair in aaPairs:
                code.append(myDict[pair] / sum)
        encodings.append(code)
    return encodings
if __name__ == '__main__':
    
    kw = {'order': 'ACDEFGHIKLMNPQRSTVWY'}
    encodings = CKSAAP(myFasta, gap = 5, **kw)
#saving extracted features
from collections import Counter
import pandas as pd
file = ('CKSAAP.tsv')
with open(file, 'w') as f:
        for i in range(len(encodings[0]) - 1):
            f.write(encodings[0][i] + '\t')
        f.write(encodings[0][-1] + '\n')
        for i in encodings[1:]:
            f.write(i[0] + '\t')
            for j in range(1, len(i) - 1):
                f.write(str(float(i[j])) + '\t')
            f.write(str(float(i[len(i)-1])) + '\n')
tsv_file=('CKSAAP.tsv')
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('CKSAAP.csv',index=False)