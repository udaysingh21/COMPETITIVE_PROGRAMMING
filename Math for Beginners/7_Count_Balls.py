if __name__=="__main__":
    # A-Blue balls and B-Red balls
    N,A,B=map(int,input().split())

    q=N//(A+B)
    r=N%(A+B)

    # Edge Test Case: 11 2 2, there might be scenario where n a+b is not exactly divisible by N but A is exactly divisible by N
    # hence we take minimum in them
    print(q*A+min(A,r))