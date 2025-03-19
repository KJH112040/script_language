from itertools import combinations
N,M = map(int,input().split())
card_num = list(map(int,input().split()))

comb = list(combinations(card_num,3))
total = [sum(t) for t in comb]
result =0

for i in total:
    if i<=M:
        if i>result:
            result=i

print(result)