# When a function calls itself direclty or indirectly, it is called Recursion.
def sumofmatrix(i,R,C,A,B,result):
    if i>=R:
        return

    for j in range(C):
        result[i][j] = A[i][j] + B[i][j]

    sumofmatrix(i+1,R, C, A, B, result)

if __name__=="__main__":
    R,C=list(map(int,input().split()))

    A,B=[],[]

    for i in range(R):
        A.append(list(map(int,input().split())))

    for i in range(R):
        B.append(list(map(int,input().split())))

    result=[]
    for i in range(R):
        result.append([0]*C)

    # print(result)
    # for i in range(R):
    #     for j in range(C):
    #         result[i][j]=A[i][j]+B[i][j]

    sumofmatrix(0, R, C, A, B, result)

    for i in range(R):
        for j in range(C):
            print(result[i][j],end=' ')
        print(' ')