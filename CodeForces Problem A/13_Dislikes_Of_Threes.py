if __name__=="__main__":
    t=int(input())
    # Brute Force Approach
    while t:
        k=int(input())

        num=1
        while k:
            if num%3==0 or num%10==3:
                num += 1
                continue
            num+=1
            k-=1

        print(num-1)

        t-=1