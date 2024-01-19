def baseconversion(n,ans):
    if n==0:
        print(ans[::-1])
        return

    ans+=str(n%2)
    baseconversion(n//2,ans)


if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())
        ans=""
        baseconversion(n,ans)

        t-=1