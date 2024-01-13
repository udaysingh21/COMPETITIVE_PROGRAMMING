if __name__=="__main__":
    H,W=map(int,input().split())

    total=0

    for i in range(H):
        strings=input()
        total+=strings.count("#")

    print(total)