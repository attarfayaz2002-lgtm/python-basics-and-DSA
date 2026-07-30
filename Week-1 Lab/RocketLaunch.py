def LaunchRocket(n):
    while n>=0:
        if n==0:
            print("Rocket Launch--")
            break
        print(n)
        n=n-1
n=int(input("Countdown starts from:"))
LaunchRocket(10)
