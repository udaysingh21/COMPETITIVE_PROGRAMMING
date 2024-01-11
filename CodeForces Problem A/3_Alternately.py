if __name__=="__main__":
    N=int(input())
    S=input()

    for i in range(1,len(S)):
        if S[i]==S[i-1]:
            print("No")
            exit()

    print("Yes")