if __name__=="__main__":
    A,B=map(int,input().split())

    sumA,sumB=0,0

    while A>0:
        r=A%10
        A=A//10
        sumA+=r

    while B>0:
        r=B%10
        B=B//10
        sumB+=r

    print(max(sumA,sumB))
