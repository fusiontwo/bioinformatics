from bioinformatics_4_1 import seq

seq_str = ''.join([i for i in seq if not i.isdigit()])
seq_strip1 = seq_str.replace('\n', '')
seq_strip2 = seq_strip1.replace(' ', '')
print("seq: ", seq_strip2.replace("//", ""))
