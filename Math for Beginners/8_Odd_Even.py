if __name__=="__main__":
    t=int(input())

    while t:
        # ans depends on prime factors
        n=int(input())

        if n%2!=0: print("Odd")
        elif n%4==0: print("Even") # 4=2**2
        else: print("Same")

        t-=1