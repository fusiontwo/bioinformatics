from bioinformatics_4_2 import seq_strip2

length = 70
string = [''.join(x) for x in zip(*[list(seq_strip2[z::length]) for z in range(length)])]
for i in string:
    print(i)
