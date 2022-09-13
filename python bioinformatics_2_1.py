while True :
    num = int(input("Which time table: "))
    if num >= 1 and num <= 9 :
        for i in range(1,10) :
            print(f"{num} * {i} = {num*i}")
    else :
        print("What?")