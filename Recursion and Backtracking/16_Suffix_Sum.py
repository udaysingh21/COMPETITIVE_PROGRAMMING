import sys
sys.setrecursionlimit(10**6)
def suffixsum(i,j,array):

    if i==len(array): return 0

    if i>=j:
        return array[i]+suffixsum(i+1,j,array)
    else:
        return suffixsum(i+1,j,array)

if __name__=="__main__":
    N,M=map(int,input().split()) # last m element summation

    array=list(map(int,input().split()))

    """Python Recursion Failed"""
    # i,j=0,N-M
    # print(suffixsum(i,j,array))

    result = 0
    for i in range(N - M, N):
        result += array[i]
    print(result)