if __name__=="__main__":
    N,Q=map(int,input().split())

    yellow=[0]*101
    red= {}

    while Q:
        # action player 1-yellow 2-red 3-ans getting 2 yellow is equivanlent to getiing red
        event=input().split()

        action=event[0]
        player=int(event[1])

        if action=='1':
            yellow[player]+=1
            # 2 yellow cards are equivalent to 1 red card
            if yellow[player]==2:
                red[player]=True

        elif action=='2':
            red[player]=True

        else:
            if player in red or yellow[player]==2:
                print("Yes")
            else:
                print("No")

        Q-=1