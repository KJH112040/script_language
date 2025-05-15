# 도로의 간선?이 재각각이면 다익스트라. 그게 아니라면 bfs?
# c++이나 파이썬 등 우선순위큐 제공
# 다익스트라 알고리즘은 시작지점에서 다른 모든 지점의 distance를 다 찾아줌. 다른 모든 노드까지의 거리
# 플로이드워셜 삼중 for문?
# 8장에서는 기타 그래프 이론이라 했는데 대표적인 최소신장트리를 배움. minimum spanning tree
# 신장 트리 spanning tree : 사이클이 존재하지 않고 모든 노드를 포함한 트리
# 최소 신장 트리는 간선이 최소화된 것.
# union-find 자료구조
#======================================================================================
# 다익스트라 (우선 순위 큐를 사용하지 않은 시간이 많이 걸리는 다익스트라)
# 입력 값
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# import sys
# input = sys.stdin.readline
# INF = int(1e9)   # 무한대값
# # 노드 간선의 개수
# n,m = map(int,input().split())
# # 시작 노드 입력
# start = int(input())
# # 노드의 연결 정보 graph 2차원 그래프
# graph = [[] for i in range(n+1)]
# # 방문처리 리스트
# visited = [False] * (n+1)
# # 최단거리 테이블 무한대로 초기화
# distance = [INF] * (n+1)
# # 간선 정보 입력 받기
# for _ in range(m):
#     a, b, c = map(int,input().split())
#     graph[a].append((b,c))
# # print(graph)
# # [[], [(2, 2), (3, 5), (4, 1)],
# #      [(3, 3), (4, 2)],
# #      [(2, 3), (6, 5)],
# #      [(3, 3), (5, 1)],
# #      [(3, 1), (6, 2)],
# #      []]
# # 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드번호 반환
# def get_smallest_node():    # 시간이 많이 걸리기 때문에 나중에 우선순위 큐로 대체
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i]<min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     visited[start] = True
#     for (adjcent, weight) in graph[start]:
#         distance[adjcent] = weight
#     # 시작노드를 제외한 n-1개 노드에 대해서 반복
#     for i in range(n-1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for (adjacent,weight) in graph[now]:
#             cost = distance[now] + weight
#             # 현재노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[adjacent]:
#                 distance[adjacent] = cost
# # 다익스트라 알고리즘 수행
# dijkstra(start)
# # 모든 노드로 가기 위한 최단거리 출력
# for i in range(1,n+1):
#     # 도달할 수 없는 경우 INFINITY 출력
#     if distance[i]==INF:
#         print("INFINITY")
#     # 도달할 수 있는 경우 거리 출력
#     else:
#         print(distance[i])
# 결과
# 0
# 2
# 3
# 1
# 2
# 4
# 이 알고리즘은 노드의 개수가 v개면 O(v^2)이 걸림.
# 중첩된 for문?
#===========================================================================
# 개선된 다익스트라 알고리즘 (이걸 외우셔야 합니다.)
# 파이썬이나 c++, 자바에 우선순위 큐가 있음
# 리스트가 편리하긴 해도 복사 패킹하는 시간이 필요
# 우선 최소 힙 사용 예제부터
# import heapq
# #오름차순 힙 정렬
# def heapsort(iterable):
#     h = []      # 최소 힙에 사용될 리스트
#     result = [] # 정렬 결과 리스트
#     # 모든 원소를 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,value)
#     # print(h)
#     # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
#     # None
#     # 힙에 삽입된 모든 원소를 차례로 꺼내서 담기
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)
# # 우선순위 큐를 사용한 개선된 다익스트라 알고리즘
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)  #  무한값을 10억으로 설정
# # 노드 개수, 간선 개수
# n,m = map(int,input().split())
# # 시작 노드
# start = int(input())
# # 노드 연결 정보 graph 만들기
# graph = [[] for _ in range(n+1)]
# # 최단거리 테이블 무한대로 초기화
# distance = [INF]*(n+1)
# # 모든 간선 정보를 입력
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
# def dijkstra(start):
#     q = []      # 최소힙에 들어갈 리스트
#     # 시작노드로 가기 위한 최단 경로는 0으로 설정하고 우선순위 큐에 삽입
#     distance[start] = 0
#     heapq.heappush(q,(0,start))
#     while q:    # q가 빌 때까지
#         # 우선순위 큐(최소힙)에서 최단거리 노드 정보를 꺼낸다.
#         dist, now = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있다면
#         if distance[now] < dist:
#             continue
#         # 현재 노드와 연결된 이웃노드 확인
#         for adjacent, weight in graph[now]:
#             cost = dist + weight
#             # 현재 노드를 거쳐서 이웃노드를 가는 거리가 짧다면 갱신
#             if cost < distance[adjacent]:
#                 distance[adjacent] = cost
#                 heapq.heappush(q,(cost,adjacent))
#
# # 다익스트라 알고리즘 수행
# dijkstra(start)
# # 모든 노드 최단 거리 출력
# for i in range(1, n+1):
#     if distance[i]==INF:
#         print("INFINITY")
#     else:
#         print(distance[i])
# 이 코드는 외우던가 어디에 잘 적어놔야 함
#====================================================================
# 우리가 게임에서 흔히 사용하는 A* 알고리즘 (a star algorithm)
# start부터 목적지까지 찾아주는 알고리즘. 다익스트라 알고리즘과 유사
# 휴리스틱 이용
#====================================================================