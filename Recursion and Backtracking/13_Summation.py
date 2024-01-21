import sys
sys.setrecursionlimit(1005)

def summation(i,N,array):
    if i>=N:
        return 0

    return array[i]+summation(i+1,N,array)

if __name__=="__main__":
    N=int(input())
    array=list(map(int,input().split()))

    print(summation(0,N,array))