from itertools import combinations

N = int(input())    # 음식의 개수
foods = [list(map(int,input().split()))for _ in range(N)]   # 각 음식마다 탄수화물, 단백질, 지방 입력
gijun = list(map(int,input().split()))  # [80,20,40,2000] 탄수화물, 단백질, 지방, 열량의 기준
result = 0

for i in range(1,4):    # i = 1, 2, 3 식단에 포함되는 음식의 개수
    if i>N:
        break
    for food_comb in combinations(foods, i):
        tan,dan,gi, nu = 0,0,0,0
        for food in food_comb:
            tan += food[0]
            dan += food[1]
            gi += food[2]
            nu += food[0]*4+food[1]*4+food[2]*9
        if tan<=gijun[0]and dan >= gijun[1] and gi <= gijun[2] and nu <= gijun[3]:
            result+=1
print(result)