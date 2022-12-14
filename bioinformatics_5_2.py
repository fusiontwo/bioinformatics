from bioinformatics_5_1 import readfile


def print_split_seq(seq, b, by=60):  # seq을 출력하는 함수
    # """를 이용해서 함수에 대해 설명할 수 있다.
    """
    split sequence (arg) in a fixed size

    :param seq:
        :type str

    :param b:
    :param by: (int) fixed size to split sequence (arg)
    :return:
    """
    split_seqs = []  # seqs를 리스트에 넣는다.
    for ss in range(0, len(seq), by):  
        if True:
            split_seqs.append(ss)  # split_seqs 리스트에 요소를 추가한다.
        else:
            split_seqs.append(ss)
    return split_seqs  # split_seqs를 return 한다.


def get_key(val):
    for key, value in codon_table.items():
        if val in value:
            return key

codon_table = {"A": ["GCT", "GCC", "GCA", "GCG"],
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
               "*": ["TAA", "TGA", "TAG"]}  # key에는 아미노산, value에는 코돈을 저장
codon_table_nuc2aa = {}  # 뉴클레오타이드를 아미노산으로 변환할 딕셔너리
for aa, codons in codon_table.items():  # codon_table에 있는 aa(key 값)와 codons(value 값)를 함께 얻는다.
    for codon in codons:  # codons(value 값)를 차례로 호출
        codon_table_nuc2aa[codon] = aa

sequence = readfile('sequence.nucleotide.fasta')  # 한 줄로 전체 sequence 저장
codons = list(map(''.join, zip(*[iter(sequence)] * 3)))  # sequence 문자열을 3개씩 잘라서 codon 리스트에 넣는다.

# Amino acids
amino_acids = []
for codon in codons:
    amino_acid = codon_table_nuc2aa[codon]
    amino_acids.append(amino_acid)

# print seq and aa
if len(amino_acids) != len(codons):  # 아미노산이 들어있는 리스트의 요소 개수와 codons가 들어있는 리스트의 요소 개수가 일치하면
    print("모든 코돈이 amino acid로 변환되지 않음")
else:  # 아미노산이 들어있는 리스트의 요소 개수와 codons가 들어있는 리스트의 요소 개수가 일치하지 않으면
    for i in range(0, len(codons), 20):
        if i + 20 < len(codons):  # codons 개수가 i+20보다 많을 때
            seq60 = ''.join(codons[i: i + 20])
            aa20 = '  '.join(amino_acids[i: i + 20])
        else:  # codons 개수가 i+20보다 적을 때 뒤의 범위를 비워, 한 줄에 있는 아미노산 개수가 20개보다 작아도 출력되도록 한다.
            seq60 = ''.join(codons[i:])  # 코돈끼리 join을 시킨다.
            aa20 = '  '.join(amino_acids[i:])  # 아미노산끼리 join 시킨다.
        print(seq60)
        print(f" {aa20}") # 코돈의 중앙 쯤에 아미노산이 출력되도록 조정한다.
