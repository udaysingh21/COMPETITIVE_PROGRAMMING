# Make sure don't print any leading or trailing spaces.
import sys
sys.setrecursionlimit(1005)

def printN1(n):
    if n==1:
        # print last one without space
        print(n)
        return

    # except for last one everyother value will be printed with space
    print(n,end=" ")
    printN1(n-1)

if __name__=="__main__":
    N=int(input())
    printN1(N)

