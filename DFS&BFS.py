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
from collections import deque


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
graph = [
    [],         # 0번 노드
    [2,3,8],    # 1번 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
# #dfs(graph,1,visited)
# dfs_stack(graph,1,visited)

#====================================
from collections import deque       # 스택이나 큐를 빠르게 구현
# 큐 BFS [ ]<- , <-[ ]
def bfs(graph,v,visited):
    queue = deque([v])          # 큐를 deque로 구현
    while queue:
        v = queue.popleft()
        if not visited[v]:
            print(v,end=' ')
            visited[v] = True
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
bfs(graph,1,visited)