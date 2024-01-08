if __name__=="__main__":
    A,B,K=map(int,input().split())

    # 1<=A,B<=100
    divisors=[]
    num=1
    while num<=100:
        if A%num==0 and B%num==0:
            divisors.append(num)
        num+=1

    print(divisors[-1*K])

