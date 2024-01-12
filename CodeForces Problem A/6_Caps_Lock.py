if __name__=="__main__":
    S=input()

    T=''
    for i in S:
        T+=chr(ord(i)-32)

    print(T)