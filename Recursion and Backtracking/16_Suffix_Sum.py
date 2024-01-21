def suffixsum(i,j,array):

    if i>=len(array): return 0

    if i>=j:
        return array[i]+suffixsum(i+1,j,array)
    else:
        return suffixsum(i+1,j,array)

if __name__=="__main__":
    N,M=map(int,input().split())

    array=list(map(int,input().split()))
    i,j=0,N-M
    print(suffixsum(i,j,array))