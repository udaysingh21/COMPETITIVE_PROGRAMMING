def factorial(n):
    # 0!=1 and 1!=1
    if n<=1: return 1

    return n*factorial(n-1)

if __name__=="__main__":
    n=int(input())

    print(factorial(n))