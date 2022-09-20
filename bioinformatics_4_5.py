for line in open('sequence.nucleotide.gb', 'r'):
    if line.startswith("  TITLE"):
        print(line)
        if "JOURNAL" in line:
            list = line.split("JOURNAL")
            print(list[0])
# TITLE 뒤에 내용이 두 줄인 경우도 있고 한 줄인 경우도 있어서, 두 줄인 경우 어떻게 읽어야 할지 모르겠다.
seq = []
# for lines in open('sequence.nucleotide.gb', 'r'):
#     print(lines)
#     for i in range(0, len(seq)):
#         seq.append(lines)
#         print(''.join(seq))
    # sequence = ''.join(seq)
    # print(sequence)


    # if line.startswith("  TITLE"):
    #     print(line)
    #     if "JOURNAL" in line:
    #         list = line.split("JOURNAL")
    #         print(list[0])
