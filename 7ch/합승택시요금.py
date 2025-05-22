# [문제]
# 지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b,
# 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다.
# 이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때,
# 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.
# 만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.
def solution(n, s, a, b, fares):
    answer = int(1e9)
    distance = [[int(1e9)]*(n+1) for _ in range(n+1)]
    for self in range(1,n+1):
        distance[self][self] = 0
    for pointA,pointB,cost in fares:
        distance[pointA][pointB] = cost
        distance[pointB][pointA] = cost
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    for k in range(1,n+1):
        answer = min(answer,distance[s][k]+distance[k][a]+distance[k][b])
    return answer

#=================교수님 코드==========================
# INF = int(1e9)      # 무한대
# def Floyd_Warshall(n,fares):
#     d = [[INF]*(n+1) for _ in range(n+1)]      # 최단거리 테이블을 INF로 초기화
#     for i in range(1,n+1):
#         d[i][i] = 0
#     for u,v,w in fares:     # u<->v 최단거리 w로 설정
#         d[u][v]=w
#         d[v][u]=w
#     # 점화식 Dab = min(Dab,Dak+Dkb)
#     for k in range(1,n+1):
#         for a in range(1,n+1):
#             for b in range(1,n+1):
#                 d[a][b] = min(d[a][b],d[a][k]+d[k][b])
#     return d
#
# def solution(n, s, a, b, fares):    # n:정점개수, s:시작점, a:A목적지, b:B목적지
#     d = Floyd_Warshall(n,fares)
#     # min(d[s][k] + d[k][a] + d[k][b])
#     answer = INF
#     for k in range(1,n+1):
#         answer = min(answer,d[s][k]+d[k][a]+d[k][b])
#     return answer
print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# 82
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# 14
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
# 28