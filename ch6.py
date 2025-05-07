# # 메모리를 적절히 재사용 -> 이미 해결한 문제를 메모리에 저장해놓고 재사용
# # dp table
# d = [0]*100
# # 피보나치 재귀함수에서 탑다운 다이나믹 프로그래밍
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     # 이미 계산한 결과가 있다면 재사용
#     if d[x] != 0:
#         return d[x]
#     # 아직 계산하지 않은 문제라면 점화식으로 재귀 호출
#     d[x] = fibo(x-1)+fibo(x-2)
#     return d[x]
#
# def fibo2(x):
#     if x == 1 or x == 2:
#         return 1
#     # 점화식으로 재귀 호출
#     return fibo2(x-1)+fibo(x-2)
#
# #print(fibo(99))
# #print(fibo2(99))
# # 결과값: 218922995834555169026
#
# d[1] = 1
# d[2] = 1
# n = 99
# # 피보나치 함수를 반복문으로 바텀업 다이나믹 프로그래밍
# for i in range(3,n+1):
#     d[i] = d[i - 1] + d[i - 2]
# print(d[n])
# # 결과값: 218922995834555169026
#
# # 분할 정복은 중복이 안 된다. ex. quick sort
# # ---> 중복이 되지 않기 때문에 다이나믹 프로그래밍으로 풀 수 없음(중복이 되지 않아 재사용 못 하기 때문)
# # 점화식을 잘 세워야 함.
#===============================================================================================
# # [문제] 개미 전사
# # 개미 전사 문제 점화식
# # ai = max(ai-1,ai-2+ki)
# # 정수 N 입력
# n = int(input())
# # 모든 식량 정보 입력
# array = list(map(int,input().split()))
# # dp table 0으로 초기화, 식량 창고 3<=N<=100
# d = [0] * 100
# # 다이나믹 프로그래밍 바텀업
# d[0] = array[0]
# d[1] = max(array[0],array[1])
# for i in range(2, n):
#     d[i] = max(d[i-1],d[i-2]+array[i])
# print(d[n-1])
# # 입력
# # 4
# # 1 3 1 5
# # 출력
# # 8
# # 입력
# # 10
# # 3 1 3 1 3 1 3 1 3 1
# # 출력
# # 15
#===========================================================
# # 정수 x 입력
# # 점화식
# # ai : i를 1로 만들기 위한 최소 연산 횟수
# # ai = min(ai-1,ai/2,ai/3,ai/5) + 1
# x  = int(input())
# # dp 테이블
# d = [0]*30001
# # d[1] = 0
# # 다이나믹 프로그래밍 바텀업
# for i in range(2, x+1):
#     d[i] = d[i-1]+1     # 1 더하기
#     if i%2==0:      # i가 2로 나눠 떨엉지면
#         d[i] = min([d[i],d[i//2]+1])
#     if i % 3 == 0:  # i가 3로 나눠 떨엉지면
#         d[i] = min([d[i], d[i // 3] + 1])
#     if i%5==0:      # i가 5로 나눠 떨엉지면
#         d[i] = min([d[i],d[i//5]+1])
# print(d[x])
#===============================================================
# # n개 화폐, m원 만들기
# # ai : i금액을 만들기 위한 최소 화폐 개수
# # a0 = 0, 나머지 ai = INF 초기화
# # ai = min(ai,ai-k + 1) for 모든 k 화폐에 대해서
# N,M = map(int,input().split())
# # n개 화폐 단위 입력
# array = [int(input()) for _ in range(N)]
# # dp 테이블 초기화
# dp = [10**9] * (M + 1)
# dp[0] = 0       # 초기화
# # 바텀업 다이나믹 프로그래밍
# for i in range(N):      # 모든 화폐종류에 대해서
#     for j in range(array[i], M+1):      # 현재 화폐 인덱스
#         if dp[j - array[i]] != 10**9:       # i-k원 만드는 방법이 존재
#             dp[j] = min(dp[j],dp[j-array[i]]+1)
# # 결과 출력
# if dp[M] == 10**9:      # M원 만드는 방법이 없음
#     print(-1)
# else:
#     print(dp[M])
#==========================================================================
# # nxm 금광에서 최대 금획득량을 얻고자 한다.
# # array[i][j]: i행 j열 금광양
# # dp[i][j]: i행 j열까지 올 때 캔 최대 금광양
# # dp[i][j] = array[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
# # 테스트 케이스 입력받고 반복문
# for tc in range(int(input())):
#     # 금광 정보 입력
#     n,m = map(int,input().split())
#     array = list(map(int,input().split()))
#     # 다이나믹 프로그래밍을 위한 dp 테이블
#     dp = []
#     index = 0
#     for i in range(n):      # n행에 대해서
#         dp.append(array[index:index+m])
#         index += m
#     # 다이나믹 프로그래밍
#     for j in range(1,m):    # 1열부터 m-1열 까지 진행
#         for i in range(n):  # dp[i][j]를 갱신하려고 한다.
#             # 왼쪽 위
#             if i==0: left_up = 0
#             else:    left_up = dp[i-1][j-1]
#             # 왼쪽 아래
#             if i==n-1: left_down = 0
#             else:      left_down = dp[i+1][j-1]
#             # 왼쪽
#             left = dp[i][j-1]
#             dp[i][j] += max(left_up,left,left_down)
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m-1])
#     print(result)
#============================================================================
n = int(input())
array = list(map(int,input().split()))
# 순서를 뒤집는다. LIS문제로 전환
array.reverse()
# dp 체이블 1로 초기화
# dp[i] : arrau[i]를 끝원소로 갖는 LIS 길이
# dp[i] = max(dp[i],dp[j]+1) if array[j] < array[i] (0<=j<=i)
dp = [1] * n
# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘
for i in range(1,n):    # i = 1,2,...,n-1
    for j in range(i):  # j = 0,1,...,i-1
        if array[j]<array[i]:
            dp[i] = max(dp[i],dp[j]+1)
# 열외해야 하는 최소 병사 수
print(n - max(dp))