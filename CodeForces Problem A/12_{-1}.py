if __name__=="__main__":
    N,X=map(int,input().split())
    values=list(map(int,input().split()))

    print(values.index(X)+1)
