# 파일1 = sequence.nucleotide.fasta
file1 = open('sequence.nucleotide.fasta', 'r')
x = file1.readlines()
seqs = []
for line in x:
    if line.startswith('>'):
        header = line.rstrip()
    else:
        seq = line.rstrip()
        seqs.append(seq)
sequence = ''.join(seqs)

# 파일2 = sequence.nucleotide.gb
file2 = open('sequence.nucleotide.gb', 'r')
y = file2.readlines()
seqs2 = []
for line in y:
    if line.startswith('LOCUS'):
        header2 = line.rstrip()
    else:
        seq2 = line.rstrip()
        seqs2.append(seq2)
sequence2 = ''.join(seqs2)
list_split = sequence2.split('ORIGIN')
sequence2 = list_split[1]
sequence2_str = ''.join([i for i in sequence2 if not i.isdigit()])
sequence2_strip = sequence2_str.replace(' ', '')
sequence2_strip2 = sequence2_strip.replace('//', '')

# 사용자 입출력
while True:
    input_file = input("Enter input file: ")
    output_file = input("Enter output file: ")
    print("""    Option-1) Read a FASTA format DNA sequence file and make a reverse sequence.
    Option-2) Read a FASTA format DNA sequence file and make a reverse complementary sequence.
    Option-3) Convert GenBank format file to FASTA format file.""")
    option = int(input("Select the option: "))

    # option 1
    if option == 1:
        print(output_file)
        print(header)
        print(sequence[::-1])

    # option 2
    if option == 2:
        print(output_file)
        print(header)
        sequence_list = []
        sequence_list = list(sequence[::-1])

        for i in range(0, len(sequence_list)):
            if sequence_list[i] == 'A':
                sequence_list[i] = 'T'
            elif sequence_list[i] == 'G':
                sequence_list[i] = 'C'
            elif sequence_list[i] == 'C':
                sequence_list[i] = 'G'
            else:
                sequence_list[i] = 'A'
        reverse_sequence = ''.join(sequence_list)
        print(reverse_sequence)

    # option 3
    if option == 3:
        print(output_file)
        print(header2)
        print(sequence2_strip2)
