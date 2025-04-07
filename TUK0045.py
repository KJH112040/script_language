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

def DFS(v,i,graph,N,visited):
    stack = deque([v])
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v]=True
        for l in range(N):
            if l != i and not visited[l] and not l in stack and graph[v][l]:
                stack.append(l)

N,M = map(int,input().split())
graph = [[False]*N for _ in range(N)]
for _ in range(M):
    i,j = map(eval,input().split())
    graph[i-1][j-1] = True
    graph[j-1][i-1] = True

answer = []

for i in range(N):
    visited = [False]*N
    v = (i+1)%N
    DFS(v,i,graph,N,visited)

    for c in range(N):
        if i != c and not visited[c]:
            answer.append(i+1)
            break
print(len(answer))
for c in answer:
    print(c)