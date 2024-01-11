if __name__=="__main__":
    N,D=map(int,input().split())
    time=list(map(int,input().split()))


    for i in range(1,len(time)):
        difference=time[i]-time[i-1]
        if difference<=D:
            print(time[i])
            exit()

    print(-1)