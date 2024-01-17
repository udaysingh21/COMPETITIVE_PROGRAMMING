import sys
sys.setrecursionlimit(1005)

def printRecursion(n):
    if n==0: return

    print("I love Recursion")
    printRecursion(n-1)


if __name__=="__main__":
    n=int(input())

    printRecursion(n)