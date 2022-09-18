infos = []
for line in open('sequence.nucleotide.gb', 'r'):
    info = line.rstrip()
    infos.append(info)
full = ''.join(infos)
after_translation = full.split('translation=')
before_exon = after_translation[1].split('exon')
result = ''.join(before_exon[0])
result_replace = result.replace(" ", "")
print(result_replace)