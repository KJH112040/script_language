from collections import deque


# def move_subin(N,sec):
#     queue = deque([(N,sec)])
#     while queue:
#         N,s = queue.popleft()
#         if N == K:
#             return s
#         if not N in visited:
#             visited.append(N)
#             for i in [N-1,N+1,2*N]:
#                 if not i in visited:
#                     queue.append((i,s+1))
#
# N, K = map(int,input().split())
# sec = 0
# visited = []
# print(move_subin(N,sec))

#=========교수님 코드===========
def bfs(N,distance):
    queue = deque([(N,distance)])       # (수빈이의 위치, 거리)
    while queue:    # 큐가 빌 때까지
        N,distance = queue.popleft()        # 큐의 제일 왼쪽에서 꺼낸다.
        if N==K:  # 동생과 만났다면 종료
          return distance
        # 3 가지 탐색 N-1,N+1, 2N
        if N-1 >= 0 and not visited[N-1]:
            visited[N-1] = True     # 방문 처리
            queue.append((N-1,distance+1))
        if N+1 <= 100000 and not visited[N+1]:
            visited[N+1] = True     # 방문 처리
            queue.append((N+1,distance+1))
        if 2*N<=100000 and not visited[2*N]:
            visited[2*N] = True  # 방문 처리
            queue.append((2*N, distance + 1))


N,K = map(int,input().split())
visited = [False]*100001    # N(0<= N <= 100,000)
visited[N] = True   # 수빈이의 현재 위치는 방문 처리
distance = 0        # 동생을 찾을 때까지 걸린 시간
print(bfs(N,distance))