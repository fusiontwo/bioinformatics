# 파일 복사
file = open('sequence.protein.fasta','r')
x = file.read()
file = open('sequence.protein.2.fasta','w')
file.write(x)
file.close()

# 파일을 열어서 한 줄씩 내용 붙여넣기(메모리 공간을 더 적게 사용)
file = open('sequence.protein.fasta')
lines = file.readlines()
file = open('sequence.protein.3.fasta','w')
for i in range(0, len(lines)):
    file.write(lines[i])