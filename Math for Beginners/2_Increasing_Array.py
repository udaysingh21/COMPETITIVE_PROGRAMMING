if __name__=="__main__":
    n=int(input())
    array=list(map(int,input().split()))

    # 1<=n<=2*10**5
    prev=array[0]
    moves=0
    for i in range(1,n):
        if array[i]<prev:
            moves=moves+(prev-array[i])
        else:
            prev=array[i]

    print(moves)
