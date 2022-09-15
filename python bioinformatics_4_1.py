file = open('sequence.protein.gb', 'r')
title = file.readlines()
print("title: ", title[0], end='')

file = open('sequence.protein.gb', 'r')
content = file.readlines()
content_join = ''.join(content)
content_divide = content_join.split("ORIGIN")
seq = content_divide[1]
seq = seq.lstrip()

print("seq: ", end='')
print("  ", seq)
file.close()
