def orangecap(dic):
    d={}
    for x in dic.values():
        for y in x:
            d[y.lower()]=d.get(y.lower(),0)+x.get(y)
    print(sorted(d,key=d.get,reverse=True)[0])
di={}    
match_count=int(input("enter the number of matches"))
for i in range(1,match_count+1):
    player_count=int(input("enter the no of players for match "+str(i)))
    di[i]={}
    for j in range(player_count):
        player_name=input("enter the player name")
        player_score=int(input("enter the player's score"))
        di[i][player_name]=player_score
orangecap(di)    
            
