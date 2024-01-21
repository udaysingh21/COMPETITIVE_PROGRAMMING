def fibonacci(n):
    if n<=1: return n

    return fibonacci(n-1)+fibonacci(n-2)

if __name__=="__main__":
    n=int(input()) # n=5 output:3    0 1 1 2 3
    n-=1
    print(fibonacci(n))