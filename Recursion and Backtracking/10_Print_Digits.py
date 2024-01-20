def printdigits(n):

    if n==0:
        print(0,end=' ')

    if n//10==0:
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