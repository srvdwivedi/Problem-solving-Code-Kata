def loop():
    try:
        n = int(input())
        for i in range(n):
            print("Hello",end=" ")
    except ValueError as e:
        print("invalid")
loop()
