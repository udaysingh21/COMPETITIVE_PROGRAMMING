def printdigits(n):
    if n==0: # base case
        print(0,end=' ')

    if n//10==0: # 1//10==0 2//10==0 3//10==0.....9//10 ie single diigt number print directly
        print(n,end=' ')

    printdigits(n//10)
    print(n%10,end=' ')

if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())
        printdigits(n)
        print(' ')
        t-=1