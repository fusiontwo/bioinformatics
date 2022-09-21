from bioinformatics_5_1 import readfile

sequence = readfile('sequence.nucleotide.fasta')  # 한 줄로 전체 sequence 저장
codon = list(map(''.join, zip(*[iter(sequence)] * 3)))  # sequence 문자열을 3개씩 잘라서 codon 리스트에 넣는다.


def codon_60(a, b):
    for i in range(a, b):
        print(codon[i], end='')


table = {"A": ["GCT", "GCC", "GCA", "GCG"],
         "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
         "N": ["AAT", "AAC"],
         "D": ["GAT", "GAC"],
         "C": ["TGT", "TGC"],
         "Q": ["CAA", "CAG"],
         "E": ["GAA", "GAG"],
         "G": ["GGT", "GGC", "GGA", "GGG"],
         "H": ["CAT", "CAC"],
         "I": ["ATT", "ATC", "ATA"],
         "M": ["ATG"],
         "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
         "K": ["AAA", "AAG"],
         "F": ["TTT", "TTC"],
         "P": ["CCT", "CCC", "CCA", "CCG"],
         "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
         "T": ["ACT", "ACC", "ACA", "ACG"],
         "W": ["TGG"],
         "Y": ["TAT", "TAC"],
         "V": ["GTT", "GTC", "GTA", "GTG"],
         "*": ["TAA", "TGA", "TAG"]}


def get_key(val):
    for key, value in table.items():
        if val in value:
            return key


protein = []
for x in range(0, len(sequence)-len(sequence) % 3, 3):
    protein.append(get_key(sequence[x:x + 3]))

for i in range(0, len(sequence), 20):
    codon_60(i, i + 20)
    print("\n")
    for n in range(i, i + 20):
        print(f"{protein[n]}  ", end='')
    print('\n')
