# from collections import deque
# def BFS(N,graph,node,visited):
#     cnt = 0
#     queue = deque([node])
#     while queue:
#         node = queue.popleft()
#         if not visited[node]:
#             visited[node] = True
#             cnt+=1
#             for i in graph:
#                 if i[0] == node:
#                     if not visited[i[1]]:
#                         queue.append(i[1])
#                 if i[1]==node:
#                     if not visited[i[0]]:
#                         queue.append(i[0])
#     return N - cnt - 1
#
# N,M = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(M)]
# save_point = []     # (중요 교차로, 중요도)
#
# cnt = 0
# for i in range(1,N):
#     save = 0
#     visited = [False]*(M+1)
#     visited[i] = True
#     if i == 1:
#         save = BFS(N,graph,2,visited)
#     else:
#         save = BFS(N,graph,1,visited)
#
#     if save != 0:
#         save_point.append((save,i))
#         cnt+=1
#
# save_point.sort()
# print(cnt)
# for i in range(len(save_point)):
#     print(save_point[i][1])
# 내꺼 runtime error & 그냥 틀린거 있는 듯

from collections import deque

# 스택 DFS, []<-,[]-> (Last In First Out)
def DFS(v,i,graph,N,visited):
    stack = deque([v])
    while stack:            # 스택이 빌 때까지
        v = stack.pop()     # 스택 제일 뒤에서 꺼냄
        if not visited[v]:      # 방문하지 않았다면
            visited[v]=True     # 방문 처리
        for l in range(1,N+1):      # j = 1,2,...,N
            # i가 아니고 방문하지 않았고 v와 연결되었으며 스택에 없다면
            if l != i and not visited[l] and not l in stack and graph[v][l]:
                stack.append(l)

N,M = map(int,input().split())              # N: 교차로 수(node), M: 도로 수(edge)
# graph[][] 2차원 배열 adjacency matrix
graph = [[False]*(N+1) for _ in range(N+1)]       # (N+1)*(N+1) 2차원 배열, graph[i][j] True라면 i<->j
# 도로 M 정보 입력
for _ in range(M):
    i,j = map(eval,input().split())
    graph[i][j] = True
    graph[j][i] = True

answer = []     # 중요한 교차로의 목록

for i in range(1,N+1):          # i = 1,2,...,N 모든 교차로에 대해서 중요한지 검사
    visited = [False]*(N+1)         # 모든 교차로 unvisited로 설정
    if i == 1:
        v = 2   # 임의의 교차로 설정
    else:
        v = 1   # 임의의 교차로 설정
    DFS(v,i,graph,N,visited)       # v에서 시작해서 완전 탐색 시도

    # i를 제외하고 unvisited 교차로가 존재하면 i는 중요한 교차로
    for c in range(1,N+1):
        if i != c and not visited[c]:
            answer.append(i)    # i는 중요한 교차로
            break
print(len(answer))      # 중요한 교차로 개수
for c in answer:        # 한줄에 하나씩 중요한 교차로 오름차순으로 출력
    print(c)