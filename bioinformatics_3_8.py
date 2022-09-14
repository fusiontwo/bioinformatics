from bioinformatics_3_6 import load_fasta
seq_d = load_fasta('sequence.protein.fasta')
seq = list(seq_d.values())[0]

while True:
    amino_acid = input("Searching for: ")
    if amino_acid == 'S':
        listA = []
        for pos, char in enumerate(seq, start=1):  # enumerate() 함수는 (인덱스, 원소)로 이루어진 튜플을 만들어준다.
            if(char == 'S'):  # 문자열이 'S'와 일치하면
                listA.append(pos)  # pos(인덱스)를 출력
        print("Found at: ", end='')  # 다음 내용을 붙여쓰기 위해서 end=''를 사용
        for i in listA:
            print(i, end=',')  # 다음 내용에 ,를 넣어 붙여쓰기 위해서 end=','를 사용
        print("\n")
    elif amino_acid == 'Q':
        listB = []
        for pos, char in enumerate(seq, start=1):  # enumerate() 함수는 (인덱스, 원소)로 이루어진 튜플을 만들어준다.
            if(char == 'Q'):
                listB.append(pos)
        print("Found at: ", end='')
        for i in listB:
            print(i, end=',')
        print("\n")
    elif amino_acid == 'XXX':
        print("Okay, I will stop.")
