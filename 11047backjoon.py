def count_coin(insertable_coin_pos):
    global cnt, K
    if K==0 or insertable_coin_pos<0: return
    else:
        if coin[insertable_coin_pos]<=K:
            cnt+=K//coin[insertable_coin_pos]
            K = K%coin[insertable_coin_pos]
        count_coin(insertable_coin_pos-1)

N,K = map(int,input().split())
coin = []
cnt = 0

for _ in range(N):
    coin.append(int(input()))

count_coin(len(coin)-1)
print(cnt)

#교수님 코드=======
#N,K = map(int,input().split())
#coins = [int(input()) for _ in range(N)]
#coins.reverse()
#result = 0
#for coin in coins:
#   result += K // coin
#   K %= coin
#   if K == 0:
#       break
#print(result)