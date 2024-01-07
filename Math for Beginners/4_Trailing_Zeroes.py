if __name__=="__main__":
    n=int(input())
    # Trailing 0 s in n! = Count of 5s in prime factors of n! = floor(n / 5) + floor(n / 25) + floor(n / 125) + ….
    # Refer GFG for better Understanding

    zeroes=0
    five=5
    # 2**x y**z = 10**z where y>=z
    while n//five>=1:
        zeroes=zeroes+n//five
        five=five*5

    print(zeroes)





