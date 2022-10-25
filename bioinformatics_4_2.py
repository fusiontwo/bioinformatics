from bioinformatics_4_1 import seq
import re

# seq_str = ''.join([i for i in seq if not i.isdigit()])
# seq_strip1 = seq_str.replace('\n', '')
# seq_strip2 = seq_strip1.replace(' ', '')
# if __name__ == "__main__":
#     print("seq: ", seq_strip2.replace("//", ""))

for c in seq:
    if ('a' <= c <= 'z'):
        seq_str = ''.join(seq)
        seq_strip1 = seq_str.replace('\n', '')
        seq_strip2 = seq_strip1.replace(' ', '')
        final_seq = re.sub(r"[0-9]", "", seq_strip2)
        # re.sub(pattern, replacement, string)는 정규표현식의 pattern과 일치하는 내용을 replacement로 변경
        # \uAC00-\uD7A30 모든 한글 음절 / a-z 영어 소문자 / A-Z 영어 대문자 / 0-9 숫자 / \s 띄어쓰기
        # 0-9앞에 ^(not)을 넣으면 반대로 숫자가 아닌 것들을 모두 제거한다.
if __name__ == "__main__":
    print("seq: ", final_seq.replace("//", ""))
