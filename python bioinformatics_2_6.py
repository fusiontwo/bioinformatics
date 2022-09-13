str = input("Enter a string: ")

str_list = list(str)  # 방법1
str_list.reverse()
print(''.join(str_list))

print(str[::-1])   # 방법2

str_reverse = ''   # 방법3
for char in str:
    str_reverse = char + str_reverse
print(str_reverse)