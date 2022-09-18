def readfile(fasta_file):
    seqs = []
    for line in open(fasta_file, 'r'):
            if line.startswith('>'):
                header = line.rstrip()
            else:
                seq = line.rstrip()
                seqs.append(seq)
            sequence = ''.join(seqs)
    return sequence

sequence = readfile('sequence.nucleotide.fasta')

codon = list(map(''.join, zip(*[iter(sequence)]*3)))  # sequence 문자열을 3개씩 잘라서 codon 리스트에 넣는다.
for i in range(0, len(codon)):
    print(codon[i])