# 파일에 문자열을 저장하고 출력하는 방법1
file = open('title.txt','w') # 쓰기 모드로 title.txt 파일을 file 객체로 연다.
file.write('This is a sequence file.') # file 객체에 문자열을 저장한다.
file.close() # file 객체를 닫는다.
file = open('title.txt','r') # 읽기 모드로 title.txt 파일을 file 객체로 연다.
x = file.read() # file 객체에서 문자열을 읽고 변수 x에 저장한다.
print(x) # 변수 x를 출력한다.
file.close() # file 객체를 닫는다.

# 문자열을 저장하고 출력하는 방법2
with open('title.txt','r')as file:
    content = file.readline()
print(content)