# find minimum prime no. greater than or equal to X

def checkprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False

    return True

if __name__=="__main__":
    x=int(input())

    counter=0
    while True:
        num=x+counter
        if checkprime(num):
            print(num)
            break
        counter+=1


