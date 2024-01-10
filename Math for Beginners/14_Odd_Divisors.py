if __name__=="__main__":
    t=int(input())

    # check if a number has only even divisors
    while t:
        number=int(input())

        while number%2==0:
            number=number//2

        if number==1: print("No")
        else: print("Yes")
        t-=1