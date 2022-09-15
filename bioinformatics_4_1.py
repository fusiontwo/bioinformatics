file = open('sequence.protein.gb', 'r')
title = file.readlines()
print("title: ", title[0], end='')

file = open('sequence.protein.gb', 'r')
content = file.readlines()
content_join = ''.join(content)
content_divide = content_join.split("ORIGIN")
seq = content_divide[1]
seq = seq.lstrip()

# 직접 이 파일을 실행하면, 조건문이 참이 되어 if 다음 문장 출력
# 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용하면, 조건문이 거짓이 되어 if 다음 문장 출력 X
if __name__ == "__main__":
    print("seq: ", end='')
    print("  ", seq.replace("//", ""))
    file.close()
