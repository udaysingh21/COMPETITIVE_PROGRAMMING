if __name__=="__main__":
    N,M=map(int,input().split())

    S=[]
    for _ in range(N):
        S.append(input())

    T={}
    for _ in range(M):
        T[input()]=True

    count=0
    for i in range(N):
        string=S[i]
        lastthree=string[-3:]
        if lastthree in T:
            count+=1

    print(count)



