import heapq
if __name__=="__main__":
    n,k=map(int,input().split())
    ids=list(map(int,input().split()))

    index={}
    for i in range(len(ids)):
        index[ids[i]]=i

    each=k//n
    remaining_candies=k%n
    ans=[each]*n

    ids.sort()

    i=0
    while remaining_candies:
        element=ids[i]
        idx=index[element]
        ans[idx]+=1
        remaining_candies-=1
        i+=1

    for i in ans:
        print(i)


