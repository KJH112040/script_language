t = int(input())
floor = []
room_num = []

for _ in range(t):
        h, w, n = map(int,input().split())
        if n%h != 0:
            floor.append(n%h)
            room_num.append(n//h + 1)
        else:
            floor.append(h)
            room_num.append(n//h)

for i in range(t):
    if room_num[i] > 9: print(f'{floor[i]}{room_num[i]}')
    else: print(f'{floor[i]}0{room_num[i]}')

#교수님 코드
#def reserve(H,W,N):    #H,W,N에 대한 방번호 반환 6 12 10
#   count = 1
#   for room in range(1,W+1):
#       for floor in range(1,H+1):
#           if count == N:
#               return floor * 100 + room
#           count += 1
#T = int(input())   #Test case 개수
#for _ in range(T)
#   H,W,N = map(int,input().split())
#   print(reserve(H,W,N))