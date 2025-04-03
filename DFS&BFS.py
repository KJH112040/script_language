# # 반복적으로 구현한 n!
# def factorial_iterative(n):
#     result = 1
#     # 1부터 n까지 수를 차례대로 곱하기
#     for i in range(1,n+1):
#         result*=i
#     return result
#
# # 재귀적으로 구현한 n!
# def factorial_recursive(n):
#     if n<=1: # n이 1이하인 경우 1을 반환
#         return 1
#     # n! = n * (n - 1)!를 그대로 코드로 작성
#     return n * factorial_iterative(n - 1)
#
# # 각각의 방식으로 구현한 n! 출력(n = 5)
# print('반복적으로 구현: ',factorial_iterative(5))
# print('재귀적으로 구현: ',factorial_recursive(5))

#=====================================================
# 스택 DFS [ ] <-, [ ]->
# def dfs_stack(graph,v,vistied):
#     stack = deque([v])      # 스택을 deque로 구현
#     while stack:            # 스택이 빌 때까지 계속
#         v = stack.pop()     # 제일 뒤에서 꺼낸다.
#         if not vistied[v]:  # 방문 하지 않았다면 방문 처리
#             print(v,end=' ')
#             vistied[v] = True   # 해당 정점 v 방문 처리
#         # v의 인접 노드들을 번호가 큰 것부터 스택에 삽입
#         for i in graph[v][::-1]:    # 번호가 큰 것부터 반대로
#             if not vistied[i]:      # 방문 하지 않았다면 스택에 넣는다
#                 stack.append(i)         # 스택 뒤에 정점 i 추가
#
# # 재귀 DFS = preorder traversal
# def dfs(graph,v,visited):
#     visited[v]=True
#     print(v,end=' ')
#     # 자식 노드 서브트리 재귀 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)
# graph = [
#     [],         # 0번 노드
#     [2,3,8],    # 1번 노드
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False]*9
# # #dfs(graph,1,visited)
# # dfs_stack(graph,1,visited)
#
# #====================================
# from collections import deque       # 스택이나 큐를 빠르게 구현
# # 큐 BFS [ ]<- , <-[ ]
# def bfs(graph,v,visited):
#     queue = deque([v])          # 큐를 deque로 구현
#     while queue:
#         v = queue.popleft()
#         if not visited[v]:
#             print(v,end=' ')
#             visited[v] = True
#             for i in graph[v]:
#                 if not visited[i]:
#                     queue.append(i)
# bfs(graph,1,visited)

#=====================================
# 얼음 얼려 먹기
# # 4 5
# # 00110
# # 00011
# # 11111
# # 00000
# # 재귀 dfs, preorder traversal: node->left subtree ->right subtree
# def dfs(r,c):   # r행 c열 위치에 대해서 검사
#     # 주어진 범위인지 검사
#     if 0<=r<n and 0<=c<m:
#         if graph[r][c]==0:
#             graph[r][c]=1   # 해당 노드 방문 처리
#             # 상하 좌우 재귀 호출
#             for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 dfs(r+dr,c+dc)
#             return True
#     return False
# n,m = map(int,input().split())  # nxm 격자
# # 2차원 리스트로 맵 정보 입력
# graph = [[int(s) for s in input()] for _ in range(n)]
# # print(graph)
# #[[0,0,1,1,0],
# # [0,0,0,1,1],
# # [1,1,1,1,1],
# # [0,0,0,0,0]]
# # 얼음의 개수
# result = 0
# for i in range(n):  # n행
#     for j in range(m):   # m열
#         if dfs(i,j)==True:  # 아직 방문하지 않은 0을 만나면
#             result +=1
#             # print('graph')
#             # print(graph)
#             # graph
#             # [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
#             # graph
#             # [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
#             # graph
#             # [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# print(result)
# # 3

#=================================
# 미로 탈출
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 10
from collections import deque
# 큐 bfs, [ ]<-, <-[ ]
def bfs(r,c):   # r행 c열 위치
    queue = deque([(r,c)])
    while queue:    # 큐가 빌 때까지
        r,c = queue.popleft()
        if r== n-1 and c==m-1:  #목적지 도달
            return graph[n-1][m-1]
        # 상하 좌우 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <n and 0<= nc < m:   # 위치 검사
                if graph[nr][nc]==1:    # 방문 하지 않은 새로운 위치를 만나면
                    graph[nr][nc] = graph[r][c] + 1
                    queue.append((nr,nc))
                    # print()
                    # # print(graph)
                    # [[1, 0, 1, 0, 1, 0], [2, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 1, 0, 1, 0], [2, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 1, 0, 1, 0], [2, 3, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 1, 0, 1, 0], [2, 3, 4, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 1, 0], [2, 3, 4, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 1, 0], [2, 3, 4, 5, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 1, 0], [2, 3, 4, 5, 6, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [1, 1, 1, 1, 1, 9], [1, 1, 1, 1, 1, 1]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [1, 1, 1, 1, 1, 9],[1, 1, 1, 1, 1, 10]]
                    #
                    # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [1, 1, 1, 1, 10, 9],[1, 1, 1, 1, 1, 10]]
                    # 교수님 왈 : "왼쪽 상단이 3으로 바뀌는 오류가 있지만 큰 차이가 안 나네요"
n,m=map(int,input().split())
# 2차원 맵
graph = [list(map(int,input())) for _ in range(n)]
dr = [-1,1,0,0] # 상하 좌우 방향 벡터
dc = [0,0,-1,1]
print(bfs(0,0)) #bfs 결과 출력