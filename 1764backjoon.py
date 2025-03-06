n,m = map(int,input().split())
np=set()
mp=set()

for _ in range(n):
    np.add(input())

for _ in range(m):
    mp.add(input())

nmp = list(np&mp)
nmp.sort()
print(len(nmp))
for p in nmp:
    print(p)