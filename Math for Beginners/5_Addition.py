if __name__=="__main__":
    n=int(input())
    numbers=list(map(int,input().split()))
    # odd number , we get LSB of number when we do and of that number lsb of odd is 1 and lsb of even is 0.

    c_odd,c_even=0,0
    for i in range(len(numbers)):
        if numbers[i]&1:
            c_odd+=1


    if c_odd&1:
        print("NO")
    else:
        print("YES")
