if __name__=="__main__":
    S=input()

    ans=0

    for char in S:
        if char=="v":
            ans+=1
        else:
            ans+=2

    print(ans)