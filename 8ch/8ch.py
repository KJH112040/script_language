# 최소신장트리(minimum spanning tree) 만드는데 필요한 자료구조 : union-find 자료구조
# union find를 쓰기 전 서로소 집합에 대해 알아야 함.
# 서로소 집합 : 서로 공통된 원소가 없는 집합
# union 합치기 find 찾기 자료구조
#==============================================================================
# 서로소 집합 자료 구조 기본적인 구현 방법
# 각 원소의 루트 찾기
# def find_parent(parent,x):
#     # 루트를 찾을 때까지 재귀
#     if parent[x]!=x:
#         return find_parent(parent, parent[x])
#     return x
#
# # 두 원소가 속한 집합을 합치기(두 원소의 루트를 같게)
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b
# # 노드와 간선의 개수 입력
# v,e = map(int,input().split())
# parent = [0] * (v+1)    # 부모 테이블
# # 부모 테이블의 부모를 자기 자신으로 초기화
# for i in range(1,v +1):
#     parent[i] = i
# # 간선마다 union 연산 수행
# for _ in range(e):
#     a,b = map(int,input().split())
#     union_parent(parent,a,b)
#
# # 각 원소가 속한 집합 출력 하기
# print('각 원소가 속합 집합:',end='')
# for i in range(1,v+1):
#     print(find_parent(parent,i),end=' ')
# print()
# # 부모 테이블 내용 출력
# print('부모 테이블:',end='')
# for i in range(1,v+1):
#     print(parent[i],end=' ')
# 출력 결과
# 각 원소가 속합 집합:1 1 1 1 5 5
# 부모 테이블:1 1 2 1 5 5
#==========================================
# 개선 (경로 압축)
# def find_parent(parent,x):
#     # 루트를 찾을 때까지 재귀
#     if parent[x]!=x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# # 두 원소가 속한 집합을 합치기(두 원소의 루트를 같게)
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b
# # 노드와 간선의 개수 입력
# v,e = map(int,input().split())
# parent = [0] * (v+1)    # 부모 테이블
# # 부모 테이블의 부모를 자기 자신으로 초기화
# for i in range(1,v +1):
#     parent[i] = i
# # 간선마다 union 연산 수행
# for _ in range(e):
#     a,b = map(int,input().split())
#     union_parent(parent,a,b)
#
# # 각 원소가 속한 집합 출력 하기
# print('각 원소가 속합 집합:',end='')
# for i in range(1,v+1):
#     print(find_parent(parent,i),end=' ')
# print()
# # 부모 테이블 내용 출력
# print('부모 테이블:',end='')
# for i in range(1,v+1):
#     print(parent[i],end=' ')
# 출력결과
# 각 원소가 속합 집합:1 1 1 1 1
# 부모 테이블:1 1 1 1 1
# 만약 기본 구현 방식이었다면,
# 1 2 3 4 5
# 1 1 2 3 4
#===========================================
# 서로소 집합을 이용한 사이클 판별
# def find_parent(parent,x):
#     # 루트를 찾을 때까지 재귀
#     if parent[x]!=x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# # 두 원소가 속한 집합을 합치기(두 원소의 루트를 같게)
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b
# # 노드와 간선의 개수 입력
# v,e = map(int,input().split())
# parent = [0] * (v+1)    # 부모 테이블
# # 부모 테이블의 부모를 자기 자신으로 초기화
# for i in range(1,v +1):
#     parent[i] = i
# # 간선마다 확인
# cycle = False
# for _ in range(e):
#     a,b = map(int,input().split())
#     # 사이클이 발생한 경우 종료
#     if find_parent(parent,a)==find_parent(parent,b):
#         cycle = True
#         break
#     # 사이클이 발생하지 않았다면 합집합
#     else:
#         union_parent(parent,a,b)
#
# if cycle:
#     print('사이클 발생')
#
# # 각 원소가 속한 집합 출력 하기
# print('각 원소가 속합 집합:',end='')
# for i in range(1,v+1):
#     print(find_parent(parent,i),end=' ')
# print()
# # 부모 테이블 내용 출력
# print('부모 테이블:',end='')
# for i in range(1,v+1):
#     print(parent[i],end=' ')
# 출력 결과
# 사이클 발생
# 각 원소가 속합 집합:1 1 1
# 부모 테이블:1 1 1
#===================================================
# 대표적인 MST 알고리즘 : 크루스칼 알고리즘
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
v,e = map(int,input().split())
parent = [0] * (v+1)    # 부모 테이블
# 부모 테이블의 부모를 자기 자신으로 초기화
for i in range(1,v +1):
    parent[i] = i
# 모든 간선 담을 리스트
edges = []
result = 0 # 최소비용 저장
# 간선마다 확인
cycle = False
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for cost, a, b in edges:
    # 사이클이 발생하지 않은 경우만 최소 신장 트리에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)

if cycle:
    print('사이클 발생')

# 각 원소가 속한 집합 출력 하기
print('각 원소가 속합 집합:',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()
# 부모 테이블 내용 출력
print('부모 테이블:',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')
#==============================================================