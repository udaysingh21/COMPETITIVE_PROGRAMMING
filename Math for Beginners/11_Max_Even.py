if __name__=="__main__":
    n=int(input())
    numbers=list(map(int,input().split()))

    numbers.sort()
    odd,even=[],[]

    for i in range(n):
        if numbers[i]&1:
            odd.append(numbers[i])
        else:
            even.append(numbers[i])

    if len(odd)<2 and len(even)<2:
        print(-1)
        exit()

    o,e=0,0
    m,n=len(odd),len(even)
    if m-2>=0: o=odd[m-1]+odd[m-2]
    if n-2>=0: e=even[n-1]+even[n-2]

    print(max(o,e))






