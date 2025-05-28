# 문제
# 동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다.
# 그러다가 평화로운 마을에 가게 되었는데, 그곳에서는 알 수 없는 일이 벌어지고 있었다.
# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다.
# 그리고 각 길마다 길을 유지하는데 드는 유지비가 있다. 임의의 두 집 사이에 경로가 항상 존재한다.
# 마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다. 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다.
# 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
# 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.
# 그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다.
# 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
# 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
# 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다.
# 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데
# A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.
#
# 임의의 두 집 사이에 경로가 항상 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.
#
# 예제 입력 1
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
# 예제 출력 1
# 8
import sys
input = sys.stdin.readline
def find_parent(parent,x):
    # 루트를 찾을 때까지 재귀
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(두 원소의 루트를 같게)
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
# 노드와 간선의 개수 입력
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
# 모든 간선 담을 리스트
edges = []
result = 0 # 최소비용 저장
# 간선마다 확인
cycle = False
for _ in range(M):
    A,B,C = map(int,input().split())
    edges.append((C,A,B))

# 간선을 비용 순으로 정렬
edges.sort()
max_cost=0
# 간선을 하나씩 확인
for C, A, B in edges:
    # 사이클이 발생하지 않은 경우만 최소 신장 트리에 포함
    if find_parent(parent,A) != find_parent(parent,B):
        union_parent(parent,A,B)
        result+=C
        max_cost = max(max_cost,C)
print(result-max_cost)

# # 교수님 코드
# def find_parent(parent,x): # 루트노드 찾기
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
# def union_parent(parent,a,b): # a,b 루트 노드를 같게
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b
# # 노드와 간선 개수 입력
# v,e = map(int,input().split())
# #부모 테이블
# parent = [0]*(v+1)
# for i in range(1,v+1):
#     parent[i] = i
# edges= []
# for _ in range(e):
#     a,b,cost = map(int,input().split())
#     edges.append((cost,a,b))
# #크루스칼 알고리즘
# edges.sort()
# # 간선을 확인
# result = 0  # 최소 신장 트리 비용 합계
# max_cost = 0 # 최소 신장 트리 간선 비용 중에서 가장 큰 값
# for cost, a,b in edges:
#     if find_parent(parent,a)!=find_parent(parent,b):
#         union_parent(parent, a, b)
#         result+=cost
#         max_cost = max(max_cost,cost)
# print(result-max_cost)  # 최소 신장 트리 비용에서 가장 큰 비용 간선 제거