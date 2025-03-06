n,m = map(int,input().split())
np=set()
mp=set()

for _ in range(n):
    np.add(input())

for _ in range(m):
    mp.add(input())

print(np&mp)