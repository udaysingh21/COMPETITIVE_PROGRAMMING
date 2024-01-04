if __name__=="__main__":
    n=int(input())
    array=list(map(int,input().split()))

    total=n*(n+1)//2
    curr_total=sum(array)

    print(total-curr_total)
