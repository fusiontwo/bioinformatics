while True :
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")

    if len(s1) % 2 != 0 and len(s1) < len(s2):
        print(s1 + s2)
    else:
        print(s2 + s1)