#importing fasta files
filenames = ['mesophilic.fas.1', 'thermophilic.fas.1']
with open('combine.fas.1', 'w') as fasta:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                fasta.write(line)
#reading fasta sequences
import re, os, sys, platform
from collections import Counter
with open('combine.fas.1') as f:
    records = f.read()   
    records = records.split('>')[1:]
    myFasta = []
    myseq = []

for fasta in records:
    array = fasta.split('\n')
    name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
    myFasta.append([name, sequence])
    myseq.append(sequence)