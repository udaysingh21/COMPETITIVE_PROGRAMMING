def restorearray(n,b,a):

    for i in range(1,n-1):
        a[i]=min(b[i],b[i-1])


# bi = max(ai, ai + 1) - b is constructed with this formulae ,
# so a will constructed with just the opposite formulae.
# just do the opposite ai=min(bi,bi-1)
if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())
        b=list(map(int,input().split()))

        a=[0]*n
        a[0]=b[0]
        a[-1]=b[-1]
        restorearray(n,b,a)

        for i in a:
            print(i,end=' ')
        print(' ')

        t-=1