t = int(input())
floor = []
room_num = []

for _ in range(t):
    while(1):
        h, w, n = map(int,input().split())
        if h >= 1 and w <=99 and n >=1 and (n <= h * w):
            if n%h != 0:
                floor.append(n%h)
                room_num.append(n//h + 1)
            else:
                floor.append(h)
                room_num.append(n//h)
            break

for i in range(t):
    if room_num[i] > 9: print(f'{floor[i]}{room_num[i]}')
    else: print(f'{floor[i]}0{room_num[i]}')