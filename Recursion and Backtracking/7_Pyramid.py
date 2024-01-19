# Don't print any space after "*"

def recursivepyramid(i,n):
    if i>=n:
        return

    for j in range(n+i):
        if j>=n-1-i:
            # we dont need delimiter after last one
            if j==n+i-1: print("*")
            else: print("*",end="")
        else: print(" ",end="")

    recursivepyramid(i+1,n)

def iterativepyramid(n):
    for i in range(n):
        for j in range(n+i):
            if j>=n-1-i:
                if j==n+i-1: print("*")
                else: print("*",end="")
            else: print(" ",end="")

if __name__=="__main__":
    n=int(input())

    # iterativepyramid(n)
    recursivepyramid(0,n)
