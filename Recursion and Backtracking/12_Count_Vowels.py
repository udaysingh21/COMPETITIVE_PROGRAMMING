if __name__=="__main__":
    string=input()

    count=0
    for s in string:
        if s in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1

    print(count)