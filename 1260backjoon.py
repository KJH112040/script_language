# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
#
# 입력 예제             출력 예제
# 4 5 1                1 2 4 3
# 1 2                  1 2 3 4
# 1 3
# 1 4
# 2 4
# 3 4
# def dfs(g,v,visited):
#     visited[v] = True
#     print(v,end=' ')
#     for i in range(1, N + 1):
#         if g[v][i] and not visited[i]:
#             dfs(g,i,visited)
#
#
# N, M, V = map(int,input().split())
# # graph 구현: adjacency matrix (N+1)*(N+1) 2차원 배열
# graph = [[False]*(N+1) for _ in range(N+1)]     # 전부 False로 초기화
# for _ in range(M):      #  M개 간선 입력
#     a,b = map(int,input().split())      # a<->b 양방향 간선
#     graph[a][b] = True
#     graph[b][a] = True
#
# dfs_visited = [False]*(N+1)
# dfs(graph,V,dfs_visited)
# print()


#================교수님 코드===============
from collections import deque
# 재귀 DFS, preorder traversal (node->left subtree->right subtree)
def DFS_rec(graph,V,visited):
    print(V,end=' ')    # node 탐색
    visited[V] = True   # 정점 V 방문 처리
    # 방문할 수 있는 정점이 여러 개인 경우 점점 번호가 작은 것을 먼저 방문
    for i in range(1,N+1):
        if graph[V][i] and not visited[i]:  # V정점의 입접 i를 방문하지 않았다면
            DFS_rec(graph, i, visited)      # 재귀 호출

# 스택 DFS
def DFS_stack(graph,V,visitied):
    stack = deque([V])      # 스택을 deque로 구현
    while stack:            # 스택이 빌 때까지
        V = stack.pop()     # 스택의 제일 뒤에서 꺼낸다.
        if not visitied[V]: # 방문 하지 않았다면 방문 처리
            print(V,end=' ')
            visitied[V]=True
        for i in range(N, 0, -1):
            if graph[V][i] and not visitied[i]:
                stack.append(i)     # 제일 뒤에 i 추가

# 큐 BFS
def BFS_queue(graph,V,visitied):
    queue = deque([V])      # 큐을 deque로 구현
    while queue:            # 큐가 빌 때까지
        V = queue.popleft()     # 큐의 제일 앞에서 꺼낸다.
        if not visitied[V]: # 방문 하지 않았다면 방문 처리
            visitied[V]=True
            print(V, end=' ')
            for i in range(1, N+1):
                if graph[V][i] and not visitied[i]:
                    queue.append(i)     # 제일 뒤에 i 추가

N, M, V = map(int,input().split())
# graph 구현: adjacency matrix (N+1)*(N+1) 2차원 배열
graph = [[False]*(N+1) for _ in range(N+1)]     # 전부 False로 초기화
for _ in range(M):      #  M개 간선 입력
    a,b = map(int,input().split())      # a<->b 양방향 간선
    graph[a][b] = True
    graph[b][a] = True

dfs_visited = [False]*(N+1)
bfs_visited = [False]*(N+1)
#DFS_rec(graph,V,visited)
DFS_stack(graph,V,dfs_visited)
print()
BFS_queue(graph,V,bfs_visited)
print()