if __name__=="__main__":
    t=int(input())

    while t:
        num=int(input())

        part=num//3

        if num%3==0:
            print(part,part)
        else:
            if num&1:
                if part%2==1:
                    print(part,part+1)
                else:
                    print(part+1,part)
            else:
                if part%2==1:
                    print(part+1,part)
                else:
                    print(part,part+1)


        t-=1