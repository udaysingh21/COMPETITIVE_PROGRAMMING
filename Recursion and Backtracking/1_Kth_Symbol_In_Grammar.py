
def kthgrammar(n,k):
    # 15/55 test cases passed
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
    return int(string[k-1])

def kthgrammar1(n,k):
    # new string = original string + replaced original string

    string='0'
    for i in range(1,n):
        length=len(string)
        for j in range(length):
            if string[j]=='0': string+='1'
            else: string+='0'

    print(string)
    return int(string[k-1])

def kthgrammar2(n,k):
    if n==1: return 0

    mid=2**(n-2) # observation
    if k<=mid: # first half
        return kthgrammar2(n-1,k) # same level with same k
    else:  # k lies in second half, in 2nd half values are negated of first half so we subtract result from 1 to get negation
        return 1-kthgrammar2(n-1,k-mid) # k is in second half so we subtract mid from k make it relative

if __name__=="__main__":
    n,k=map(int,input().split())

    # print(kthgrammar(n,k))
    # print(kthgrammar1(n,k))
    print(kthgrammar2(n,k))
