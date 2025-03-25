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

#교수님 코드==============
#from itertools import combinations
#N,M = map(int,input().split())
#cards = list(map(int,input().split()))
#maximum = 0
#for c in combinations(cards,3):
#   if sum(c)<=M:
#       maximum = max(maximum,sum(c))
#print(maximum)