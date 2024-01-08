import math

if __name__=="__main__":
    k=int(input())

    total=0
    # using 3 loops we can get all combinations
    for i in range(1,k+1):
        for j in range(1,k+1):
            for k in range(1,k+1):
                total+=math.gcd(math.gcd(i,j),k)

    print(total)
