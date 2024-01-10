def checkprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False

    return True

if __name__=="__main__":
    n=int(input())
    # 1<x,y<n
    start,end=2,n-1

    while start<end:
        if start+end>n: end-=1
        elif start+end<n: start+=1
        else:
            # if its not prime then its composite
            if not checkprime(start) and not checkprime(end):
                print(start, end)
                break

            # if its not composite then inc. start and dec. end
            start+=1
            end-=1


