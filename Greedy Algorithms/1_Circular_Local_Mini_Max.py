# Greedy Approach: Sort the array

def circular(n,arr,ans):
    arr.sort() # greedy approach
    mid=n//2

    j,k=0,mid
    for i in range(n):
        if i%2==0: # even 0,2,4...
            ans[i]=arr[j]
            j+=1
        else: # odd 1,3,5...
            ans[i]=arr[k]
            k+=1


    for i in range(1,n-1):
        # strictly greater
        if ans[i-1]<ans[i] and ans[i]>ans[i+1]:
            continue
        # strictly smaller
        elif ans[i-1]>ans[i] and ans[i]<ans[i+1]:
            continue
        else:
            return "NO"

    return "YES"


if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())
        array=list(map(int,input().split()))

        if len(array)%2==1: print("NO")
        else:
            ans=[0]*n
            result=circular(n,array,ans)
            if result=="YES":
                print("YES")
                for i in ans:
                    print(i,end=' ')
                print(' ')
            else:
                print("NO")

        t-=1