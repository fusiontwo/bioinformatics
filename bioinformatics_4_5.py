line_continued = ' ' * 12

title_line_flag = False
title_line_list = []
for line in open('sequence.nucleotide.gb', 'r'):
    if line.startswith("  TITLE"):
        title_line_flag = True
        title_line_list.append(line)
        continue

    if title_line_flag is True:
        if line[0:12] == line_continued:
            title_line_list.append(line)

        else:
            mola = ''.join(title_line_list)
            print(mola)

            title_line_flag = False
            title_line_list = []
