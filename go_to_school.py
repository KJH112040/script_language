# 문제 설명
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다.
# 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
#
# 아래 그림은 m = 4, n = 3 인 경우입니다.
#
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
#
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를
# 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
# 입출력 예
# m	n	puddles	    return
# 4	3	[[2, 2]]	4
# d[r][c] : r행 c열 격자까지 갈 수 있는 최단 경로의 개수
# d[r][c] = dp[r-1][c]+dp[r][c-1] if r행 c열 격자가 물웅덩이 아니라면
# d[r][c] = 0 if r행 c열 격자가 물웅덩이라면
def solution(m, n, puddles):
    way = [[0]*m for _ in range(n)]
    for rc in puddles:
        way[rc[1]-1][rc[0]-1] = -1
    way[0][0] = 1
    for i in range(n):
        for j in range(m):
            if way[i][j]==-1:
                way[i][j] = 0
            else:
                if i>0:
                    way[i][j] = way[i-1][j]
                if j>0:
                    way[i][j]+=way[i][j-1]
    answer = way[n-1][m-1] % 1000000007
    return answer
#===============교수님 코드============================
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for _ in range(n)]              # n행 m열 dp테이블 0으로 초기화

    puddlesList = [[0]*m for _ in range(n)]     # n행 m열 물웅덩이 2차원 배열 0으로 초기화
    for [c,r] in puddles:
        puddlesList[r-1][c-1] = 1
    # d[r][c] : r행 c열 격자까지 갈 수 있는 최단 경로의 개수
    # d[r][c] = dp[r-1][c]+dp[r][c-1] if r행 c열 격자가 물웅덩이 아니라면
    # d[r][c] = 0 if r행 c열 격자가 물웅덩이라면
    dp[0][0] = 1
    for r in range(n):
        for c in range(m):
            if puddlesList[r][c]==1:
                dp[r][c] = 0
            else:
                if r>0:
                    dp[r][c] = dp[r-1][c]
                if c>0:
                    dp[r][c] += dp[r][c - 1]
    answer = dp[n-1][m-1] % 1000000007
    return answer
print(solution(4,3,[[2,2]]))