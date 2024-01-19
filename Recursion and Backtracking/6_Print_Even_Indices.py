def printindices(i,n,array):
    if i>=n:
        return

    printindices(i+2,n,array)
    print(array[i],end=" ")


if __name__=="__main__":
    n=int(input())
    array=list(map(int,input().split()))

    printindices(0,n,array)