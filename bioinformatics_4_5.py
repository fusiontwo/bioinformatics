line_continued = ' ' * 12  # TITLE이 포함된 행의 아래 행은 공백 12칸으로 시작

title_line_flag = False  # 기본 flag를 False로 설정(전역 변수로 선언할 것)
title_line_list = []  # TITLE이 포함된 행을 넣을 리스트 생성(전역 변수로 선언할 것)
for line in open('sequence.nucleotide.gb', 'r'):  # 파일의 각 줄을 모두 읽는다.
    if line.startswith("  TITLE"):
        title_line_flag = True  # 문장이 "  TITLE"로 시작하면 flag를 True로 변환
        title_line_list.append(line)  # TITLE이 포함된 행을 리스트에 추가
        continue  # 위의 if문이 True이면 continue 아래 문장을 실행하지 않고 건너뛴다.

    if title_line_flag is True:  # flag가 True라면
        if line[0:12] == line_continued:  # line의 0~11번째 글자가 line_continued(공백 12칸)와 일치하면
            title_line_list.append(line)  # 해당 line을 리스트에 추가

        else:
            mola = ''.join(title_line_list)  # 리스트를 문자열로 출력
            print(mola)

            title_line_flag = False  # flag를 False로 초기화
            title_line_list = []  # list를 초기화
