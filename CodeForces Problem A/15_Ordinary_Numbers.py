if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())

        num=1
        ans=0
        while num<=n:
            for i in range(1,10):
                if num*i<=n:
                    ans+=1

            num=num*10+1

        print(ans)
        t-=1