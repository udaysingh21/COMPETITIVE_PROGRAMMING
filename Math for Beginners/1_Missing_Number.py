if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))

    total=n*(n+1)//2
    curr_total=sum(arr)

    print(total-curr_total)
