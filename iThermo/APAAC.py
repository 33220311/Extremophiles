# 2-APAAC
dataFile = re.sub('codes$', '', pPath )+ r'/PAAC.txt' if platform.system() == 'Windows' else re.sub('codes$', '', pPath) + '/PAAC.txt'
lambdaValue,w = 30,0.05
with open(dataFile) as f:
    records = f.readlines()
    AA = ''.join(records[0].rstrip().split()[1:])
    AADict = {}
for i in range(len(AA)):
    AADict[AA[i]] = i
    AAProperty = []
    AAPropertyNames = []
    for i in range(1, len(records) - 1):
        array = records[i].rstrip().split() if records[i].rstrip() != '' else None
        AAProperty.append([float(j) for j in array[1:]])
        AAPropertyNames.append(array[0])
AAProperty1 = []
for i in AAProperty:
    meanI = sum(i) / 20
    fenmu = math.sqrt(sum([(j - meanI) ** 2 for j in i]) / 20)
    AAProperty1.append([(j - meanI) / fenmu for j in i])
encodings = []
header = ['#']
for i in AA:
    header.append('Pc1.' + i)
for j in range(1, lambdaValue + 1):
    for i in AAPropertyNames:
        header.append('Pc2.' + i + '.' + str(j))
encodings.append(header)
for i in myFasta:
    name, sequence = i[0], re.sub('-', '', i[1])
    code = [name]
    theta = []
    for n in range(1, lambdaValue + 1):
        for j in range(len(AAProperty1)):
            theta.append(sum([AAProperty1[j][AADict[sequence[k]]] * AAProperty1[j][AADict[sequence[k + n]]] for k in
                              range(len(sequence) - n)]) / (len(sequence) - n))
    myDict = {}
    for aa in AA:
        myDict[aa] = sequence.count(aa)

    code = code + [myDict[aa] / (1 + w * sum(theta)) for aa in AA]
    code = code + [w * value / (1 + w * sum(theta)) for value in theta]
    encodings.append(code)
import pandas as pd
file = ('APAAC.tsv')
with open(file, 'w') as f:
    
        for i in range(len(encodings[0]) - 1):
            f.write(encodings[0][i] + '\t')
        f.write(encodings[0][-1] + '\n')
        for i in encodings[1:]:
            f.write(i[0] + '\t')
            for j in range(1, len(i) - 1):
                f.write(str(float(i[j])) + '\t')
            f.write(str(float(i[len(i)-1])) + '\n')
tsv_file=('APAAC.tsv')
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('APAAC.csv',index=False)