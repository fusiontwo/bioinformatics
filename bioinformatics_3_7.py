# try, except 예외 처리를 사용한 version

from bioinformatics_3_6 import load_fasta  # bioinformatics_3_6 파일에서 load_fasta 함수를 불러온다.

seq_d = load_fasta('sequence.protein.fasta')  # load_fasta 함수에 인자(fasta 파일명)를 넣는다.
seq = list(seq_d.values())[0]  # seq_d의 values를 리스트화하고 인덱스 0을 seq에 저장한다.
while True:
    num = input("Position: ")  # Position을 입력받는다.

    try:  # 이 문제에서는 try, except 대신 if, else를 사용하는 것이 좋다.(질문: Python console창에서 len(seq)을 출력하는 방법)
        if num == "XXX":
            print("Okay, I will stop.")
            break
        else :
            print(f"Three amino acids: {seq[int(num) - 1]}{seq[int(num)]}{seq[int(num) + 1]}")
    except IndexError:
        print("출력 가능한 범위가 아닙니다.")

# EOF
