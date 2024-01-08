import math

if __name__=="__main__":
    t=int(input())

    while t:
        n=int(input())
        if n == 2:
            print("Same")
            t -= 1
            continue

        odd_divisors = []
        even_divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if i%2==1:
                    odd_divisors.append(i)
                else:
                    even_divisors.append(i)


        if len(odd_divisors)>len(even_divisors): print("Odd")
        elif len(odd_divisors)<len(even_divisors): print("Even")
        else: print("Same")

        t-=1