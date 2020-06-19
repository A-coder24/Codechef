tests=int(input())
for _ in range(tests):
    total_dis=int(input())
    arr=list(map(int,input().split()))
    dishes=arr.pop(0)
    dish_dist={}
    total=1
    for i in range(0,dishes*2,2):
        dish_dist[arr[i]]=arr[i+1]
        total+=arr[i+1]
    brr=list(map(int,input().split()))
    clans=brr.pop(0)
    clan_dist={}
    for i in range(0,clans*3,3):
        clan_dist[brr[i]]=[brr[i+1],brr[i+2]]

    friends=0
    people=1
    extras=1
    for i in range(1,total_dis):
        if i in clan_dist:
            if clan_dist[i][1]<=people:
                people+=clan_dist[i][0]-1
            else:
                extras+=clan_dist[i][1]-people
                people+=clan_dist[i][1]-people
                if people> total :
                    people-=clan_dist[i][1]-people
                    extras-=clan_dist[i][1]-people

                else:
                    people+=clan_dist[i][0]-1
        
        if i in dish_dist:
            if people>dish_dist[i]:
                people-=dish_dist[i]
            else:
                print(dish_dist[i],people)
                friends+=dish_dist[i]-people+1
                people=1
    print(friends+extras)