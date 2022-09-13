# 방법 1. fasta file 불러오기를 함수로 정의

def load_fasta(fasta_file):  # fasta file을 불러오는 함수 정의
    d = {}  # header : sequence
    seqs = []  # 비어 있는 리스트 선언
    for line in open(fasta_file, 'r'):  # readlines 대신 써도 된다.
        if line.startswith('>'):  # startswith()는 문자열이 특정 문자로 시작하는지 여부를 알려준다.
            header = line.rstrip()  # rstrip()은 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.
            d[header] = ''
        else:
            seq = line.rstrip()  # line의 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.
            seqs.append(seq)  # 비어있던 seqs 리스트에 seq을 넣는다.
    d[header] = ''.join(seqs)  # '구분자'.join(리스트) : 리스트의 갑과 값 사이에 구분자를 넣어서 하나의 문자열로 합친다.
    return d  # load_fasta 함수는 d를 반환한다.

d = load_fasta('sequence.protein.fasta')  # 함수에 인자(fasta 파일명)를 넣는다.
print(list(d.values())[0])  # 딕셔너리 d의 values 값을 리스트화 하고 인덱스 0으로 호출한다. (어차피 인덱스 0만 존재하지만!)

# 방법 2. fasta file을 직접 불러오고, line_a를 return
def bio3_6():
    file = open('sequence.protein.fasta','r')  # fasta file을 연다.
    lines = file.readlines()  #
    print("title: ", lines[0])
    str = "seq:"
    print(str.replace("\n",""))
    for line in lines[1:len(lines)] :
        line_a = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
        print(line_a)
    file.close()
    return line_a