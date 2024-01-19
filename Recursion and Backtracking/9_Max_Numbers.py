def recursivemax(i,maxi,n,array):
    if i>=n:
        print(maxi)
        return

    if array[i]>maxi: maxi=array[i]
    recursivemax(i+1,maxi,n,array)

if __name__=="__main__":
    n=int(input())
    array=list(map(int,input().split()))

    recursivemax(0,float("-inf"),n,array)
