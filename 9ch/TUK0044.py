# [2020 본선 H] 목재 총량
# Description
#
# 숲은 직사각형 모양이며 나무는 균등 한 간격으로 배열되어 있습니다.
# 나무의 높이와 둘레가 다르기 때문에 목재 값은 나무마다 다릅니다.
# 산림청은 각 나무에 대한 데이터를 수집했으며 숲의 각 나무에서 사용할 수있는 나무의 양 (입방 피트)을 알고 있습니다.
#
# 산림청은 이 정보를 정수의 M×N 배열 형태로 유지합니다. 여기서(i, j) 항목은 i번째 행의 j번째 나무의 양 (입방 피트)입니다.
# 행은 위에서 아래로 번호가 매겨지고 열은 왼쪽에서 오른쪽으로 번호가 매겨진다고 가정합니다.
#
# 예를 들어 배열이 다음과 같습니다.
#
# 3  4  15 23
# 14 20 12 9
# 3  8  12 15
# 12 20 7  5
#
# 위 배열의 위치 (3,4)에 있는 나무의 양은 15 입방 피트 입니다.
#
# 산림청은 숲의 직사각형의 토지에 목재의 총량을 계산하여 토지 임대 자료로 활용하려고 합니다.
# 직사각형은 왼쪽 상단 모서리와 오른쪽 하단 모서리의 나무 위치로 나타냅니다.
# 예를 들어서 위치 (2,2) 와 (3,4) 모서리를 가지는 직사각형은 아래 그림과 같습니다.
#
# 20 12 9
# 8  12 15
#
# 이 직사각형 토지의 목재 총량은 76 입방 피트입니다.
# 마찬가지로 직사각형 모서리가 (4,2)와 (4,2)인 경우의 목재양은 하나 뿐인 나무의 양 20 입방 피트입니다.
# 당신의 임무는 삼림청에서 지정한 직사각형 토지의 목재 총량을 계산하는 것입니다.
#
# Input
# 입력의 첫 번째 줄에는 숲의 나무 행과 열을 나타내는 두 개의 정수 M과 N
# 다음 M개 줄에는 각각 N개의 정수가 있습니다.
# 숲의 i행 j열 위치의 나무 양은 입력의 i+1번째 줄의 j번째 정수로 나타냅니다.
# M+2번째 줄에는 목재 총량을 계산해야 하는 직사각형 토지의 개수 C를 나타냅니다.
# 이어지는 C개 줄 (M+2+1번째 줄 ... M+2+C번째 줄)에는 4개의 정수 r1, c1, r2, c2 (r1≤r2, c1≤c2)가 직사각형의 2개 모서리를 나타냅니다.
# (r1,c1)은 좌측 상단 모서리, (r2,c2)는 우측 하단 모서리를 나타냅니다.
# 2 ≤M≤ 1000, 2 ≤N≤ 1000,C≤ 1000000입니다.
# 입력의 30% 는C≤ 100 입니다.
# 목재 총량을 계산해야 하는 직사각형 토지 개수 C가 매우 큰 수 입니다.
#
# Output
# 출력의 C개 줄에는 각각 직사각형 토지의 목재 총량의 정수를 출력합니다.
# 즉 출력의 i번째 줄에는 입력의 M+2+i번째 줄에서 설명한 직사각형 토지의 목재 총량을 출력합니다.
#
#
# Sample Input 1
# 4   4
# 3   4   15  23
# 14  20  12  9
# 3   8   12  15
# 12  20  7   5
# 2
# 2   2   3   4
# 4   2   4   2
# Sample Output 1
# 76
# 20
#
# Hint
# 단순한 알고리즘은 시간초과를 극복할 수 없습니다.
# 동적 계획법(Dynamic Programming) (https://ko.wikipedia.org/wiki/동적계획법)
# 일반적으로 주어진 문제를 풀기 위해서, 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음,
# 그것을 결합하여 최종적인 목적에 도달하는 것이다.
# 각 하위 문제의 해결을 계산한 뒤, 그 해결책을 저장하여 후에 같은 하위 문제가 나왔을 경우 그것을 간단하게 해결할 수 있다.
# 이러한 방법으로 동적 계획법은 계산 횟수를 줄일 수 있다. 특히 이 방법은 하위 문제의 수가 기하급수적으로 증가할 때 유용하다.
#
# DP == prefix_sum 목재 총량
# prefix_sum을 점화식으로 나타낼 수 있음. dynamic programming 임.
# R = [][]      # 주어진 M행 N열 2차원 나무 배열
# dp[r][c] : (0,0) 에서 (r,c)까지 직사각형 토지의 목재 총량 정의
# 점화식
# (0,0)------------------------------------
# -----------------------------------------
# ---------(r-1,c-1)(r-1,c)----------------
#----------(r,  c-1)(r,  c)----------------
# dp[r][c] = dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1] + R[r][c]
# (r1,c1) : (r2,c2) 부분합 = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
# -----------------------------
#      |                    |
# (r1-1,c-1)-----------(r1-1,c2)
# -----|----(r1,c1)------------
#      |        |           |
#      |        |           |
#      |        |           |
# (r2,c1-1)--------------(r2,c2)
M,N = map(int,input().split())      # M행 N열
R = [list(map(int,input().split())) for _ in range(M)]      # MxN 2차원 목재 배열
# DP == prefix_sum 목재 총량
# prefix_sum을 점화식으로 나타낼 수 있음. dynamic programming 임.
# R = [][]      # 주어진 M행 N열 2차원 나무 배열
# dp[r][c] : (0,0) 에서 (r,c)까지 직사각형 토지의 목재 총량 정의
# 점화식
# (0,0)------------------------------------
# -----------------------------------------
# ---------(r-1,c-1)(r-1,c)----------------
#----------(r,  c-1)(r,  c)----------------
# dp[r][c] = dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1] + R[r][c]
dp = [[0] * (N+1) for _ in range(M+1)]      # (M+1)x(N+1) 2차원 dp 테이블 0으로 초기화
for r in range(1,M+1):      # r = 1,2,...,M
    for c in range(1,N+1):  # c = 1,2,...,N
        dp[r][c] = dp [r][c-1] + dp[r-1][c] - dp[r-1][c-1] + R[r-1][c-1]
# print(dp)
# [[0, 0, 0, 0, 0],
# [0, 3, 7, 22, 45],
# [0, 17, 41, 68, 100],
# [0, 20, 52, 91, 138],
# [0, 32, 84, 130, 182]]
C = int(input())        # 테스트 데이터의 개수
# (r1,c1) : (r2,c2) 부분합 = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
# -----------------------------
#      |                    |
# (r1-1,c-1)-----------(r1-1,c2)
# -----|----(r1,c1)------------
#      |        |           |
#      |        |           |
#      |        |           |
# (r2,c1-1)--------------(r2,c2)
for _ in range(C):
    r1,c1,r2,c2 = map(int,input().split())
    print(dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1])