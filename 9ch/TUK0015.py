# b 진법
# Description
# b 진수 숫자(b>0)의 모든 숫자는 0과 b-1 사이의 숫자입니다.
# 예를 들어 기수 4를 가지는 4진수 숫자는 3312 또는 30을 쓸 수 있습니다.
# b 진수 숫자가 dn-1 ... d0이고 각 di가 0과 b-1 사이에 있다고 가정하면 그 숫자의 10진수는 다음과 같이 계산할 수 있습니다.
# dn-1 ... d0 (b진수) =d0 + d1 * b + d2 * b^2 + ... + di * b^i + ... + dn-1 * b^(n-1) (10진수)
#
# 우리는 숫자 표현에서 앞자리 0을 허용하지 않습니다. 예를 들어, 3312 대신 003312 또는 03312를 쓸 수 없습니다.
#
# 10 진수로 주어진 숫자는 위의 계산을 거꾸로하여 b진수 표현을 계산할 수 있습니다.
#
# 3312 (4진수) = 246 (10진수)
# 30 (4진수) = 12 (10진수)
# 2  11  10 (12진수, 빈 공간을 사용하여 숫자 구분) = 430 (10진수)
# 3  0  2 (12진수) = 434 (10진수)
#
# 당신의 임무는 기수 b와 b진수 숫자 A와 B가 제공되면 A × B의 b 진수 숫자를 출력하는 것입니다.
# 예를 들면 다음과 같습니다.
#
# 3312 (4진수) x 30 (4진수) = 232020 (4진수)
# 2  2  10  10 (12진수) x 3 0 2 (12진수) = 8  11  11  11  8 (12진수)
#
# Input
# 첫 번째 행에는 3 개의 정수 b, N 및 M이 포함되며 여기서 b는 기수입니다.
# N과 M은 주어진 두 숫자의 b진수 표현의 숫자 개수입니다.
# 두 번째 줄은 N 개의 공백으로 구분 된 정수로써 DN-1 DN-2 ... D0은 첫 번째 숫자의 b진수 표현을 제공합니다.
# 세 번째 줄은 M 개의 공백으로 구분 된 정수로써 EM-1 EM-2 ... E0는 두 번째 숫자의b진수 표현을 제공합니다.
# 1 ≤ N, M ≤ 1000이라고 가정
#
# Output
# 첫 번째 행은 곱의 b 진수 숫자 개수를 나타내는 단일 정수 L이어야합니다.
# 두 번째 줄에는 b 진수 표현을 제공하는 L 공백으로 구분 된 정수가 포함되어야합니다.
#
# Sample Input 1
# 4 4 2
# 3 3 1 2
# 3 0
# Sample Output 1
# 6
# 2 3 2 0 2 0
#
# Sample Input 2
# 12 3 3
# 2 11 10
# 3 0 2
# Sample Output 2
# 5
# 8 11 11 11 8
b, n, m = map(int,input().split())
d = list(map(int,input().split()))
e = list(map(int,input().split()))
#1차 시도====================================
#a = [[] for _ in range(m)]
# cnt = 0
# for ei in range(len(e) - 1, -1, -1):
#     for _ in range(cnt):
#         a[cnt].append(0)
#     add_num = 0
#     for di in range(len(d)-1,-1,-1):
#         mul_num = d[di] * e[ei]
#         num = mul_num + add_num
#         a[cnt].append(num%b)
#         add_num = num // b
#     if add_num != 0:
#         a[cnt].append(add_num)
#     cnt+=1
#
# add_n = 0
# for j in range(len(a[cnt-1])):
#     num = 0
#     for i in range(m):
#         if j < len(a[i]):
#            num += a[i][j]
#         else:
#             continue
#     a[cnt-1][j] = (add_n + num) % b
#     add_n = (add_n + num) // b
# if add_n != 0:
#     a[cnt-1].append(add_n)
# print(len(a[cnt-1]))
# for i in range(len(a[cnt-1]) - 1,-1,-1):
#     print(a[cnt-1][i],end=' ')
#=========================================
# 2차 시도
def num(a):
    l = len(a) - 1
    num = 0
    for i in range(l,-1,-1):
        num += a[i] * (b ** (l-i))
    return num
d_num = num(d)
e_num = num(e)
num = d_num * e_num
a = []
while num // b:
    a.append(num%b)
    num //= b
if num != 0:
    a.append(num)
print(len(a))
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')