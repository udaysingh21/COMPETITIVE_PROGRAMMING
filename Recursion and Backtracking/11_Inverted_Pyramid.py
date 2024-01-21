def recursivepyramid(n):
    m=n
    for i in range(n):
        for j in range(n*2-i-1):
            if j<n-m: print(' ',end=' ')
            elif j==n*2-i-2: print('*',end='\n')
            else: print('*',end=' ')
        m-=1
        # print('\n')


if __name__=="__main__":
    n=int(input())

    recursivepyramid(n)
    # invertedpyramid(n)