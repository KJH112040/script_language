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