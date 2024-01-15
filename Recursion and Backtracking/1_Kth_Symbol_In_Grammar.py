
def kthgrammar(n,k):
    string='0'

    for i in range(1,n):
        new=''
        for j in range(len(string)):
            if string[j]=="0":
                new+="01"
            else:
                new+="10"
        string=new

    print(string)
    return string[k-1]

if __name__=="__main__":
    n,k=map(int,input().split())

    print(kthgrammar(n,k))
