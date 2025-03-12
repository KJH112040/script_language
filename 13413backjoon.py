def change(N,s,e):
    BtoW = 0
    WtoB = 0
    for i in range(N):
        if s[i] != e[i]:
            if s[i]=='B': BtoW+=1
            else: WtoB+=1
    swap = max(WtoB,BtoW)
    flip = BtoW+WtoB
    return min(swap,flip)

T = int(input())

for _ in range(T):
    N,s,e = int(input()),input(),input()
    print(change(N,s,e))

#=====교수님 코드=====
#T = int(input())           테스트 케이스 개수
#for _ in range(T):         T번 반복
#   N = int(input())        말의 개수
#   orig = input()          초기 상태
#   goal = input()          목표 상태
#   BW = 0
#   WB = 0
#   for i in range(N):      0,1,...,N-1
#       if orig[i] == 'B' and goal[i] == 'W':
#           BW+=1
#       if orig[i] == 'W' and goal[i] == 'B':
#           WB+=1
#   print(max(BW,WB))       BW = 5, WB = 3, 이면 3 번은 서로 위치를 바꾸고, 나머지 2 번은 돌을 뒤집는다.