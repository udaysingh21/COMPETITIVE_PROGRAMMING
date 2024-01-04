if __name__=="__main__":
    t=int(input())
    # kisi bhi number ka 1 ke saath & and krte hai to wo us number ka lsb deta hai aur odd ka lsb 1 hota hai
    # aur even ki lsb 0 hoti hai
    while t:
        x,y=list(map(int,input().split()))
        d=max(x,y)
        d_ele=d**2-d+1
        if d&1: # odd number
            if y>x:
                d_ele+=(y-x)
            else:
                d_ele-=(x-y)
        else:
            if y>x:
                d_ele-=(y-x)
            else:
                d_ele+=(x-y)

        print(d_ele)
        t-=1