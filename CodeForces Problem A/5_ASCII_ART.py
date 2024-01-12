if __name__=="__main__":
    H,W=map(int,input().split())

    A=[list(map(int,input().split())) for _ in range(H)]

    dicti={}
    for i in range(1,27):
        dicti[i]=chr(64+i)

    for i in range(H):
        ans = ''
        for j in range(W):
            if A[i][j]==0:
                ans+='.'
            else:
                ans+=dicti[A[i][j]]

        print(ans)
