import sys
sys.setrecursionlimit(1005)

def printN(n):
    if n==0: return

    printN(n-1)
    print(n)

if __name__=="__main__":
    N=int(input())

    printN(N)