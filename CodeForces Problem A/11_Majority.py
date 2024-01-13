if __name__=="__main__":
    N=int(input())

    forcount=0
    foragsinst=0

    for i in range(N):
        opinion=input()
        if opinion=="For":
            forcount+=1
        else:
            foragsinst+=1

    if forcount>foragsinst: print("Yes")
    else: print("No")