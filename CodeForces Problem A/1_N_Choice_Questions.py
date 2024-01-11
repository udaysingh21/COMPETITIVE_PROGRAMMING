if __name__=="__main__":
    N,A,B=map(int,input().split())
    choices=list(map(int,input().split()))

    total=A+B
    print(choices.index(total)+1)