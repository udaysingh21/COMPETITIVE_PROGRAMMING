if __name__=="__main__":
    N=int(input())
    A=list(map(int,input().split()))

    for ele in A:
        if not ele&1:
            print(ele,end=" ")