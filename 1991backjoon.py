# 이진 트리를 입력받아
# 전위 순회(preorder traversal),
# 중위 순회(inorder traversal),
# 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
#
#
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
#
# 출력
# 첫째 줄에 전위 순회,
# 둘째 줄에 중위 순회,
# 셋째 줄에 후위 순회한 결과를 출력한다.
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
#
# 입력 예제
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
#
# 출력 예제
# ABDCEFG
# DBAECFG
# DBEGFCA
# N = int(input())            # 노드의 개수
# binary_tree = {}            # 트리는 사전으로 구성, key:value = 노드:[왼쪽 자식, 오른쪽 자시]
# preorder_traverse = []
# inorder_traverse = []
# postorder_traverse = []
#
# for _ in range(N):
#     root, left, right = map(int,input().split())
#     binary_tree[root]  = {'Left':left, 'Right':right}
#
# root = 'A'
# while True:
#     preorder_traverse.append(root)
#     if
#
#=====교수님 코드=======
def preorder(node):
    if node != '.':     # 노드가 null이 아니면
        print(node,end='')
        preorder(binary_tree[node][0])      # 왼쪽 서브 트리 순회
        preorder(binary_tree[node][1])      # 오른쪽 서브 트리 순회

def inorder(node):
    if node != '.':     # 노드가 null이 아니면
        inorder(binary_tree[node][0])      # 왼쪽 서브 트리 순회
        print(node,end='')
        inorder(binary_tree[node][1])      # 오른쪽 서브 트리 순회

def postorder(node):
    if node != '.':     # 노드가 null이 아니면
        postorder(binary_tree[node][0])  # 왼쪽 서브 트리 순회
        postorder(binary_tree[node][1])  #   오른쪽 서브 트리 순회
        print(node,end='')

N = int(input())            # 노드의 개수
binary_tree = {}            # 트리는 사전으로 구성, key:value = 노드:[왼쪽 자식, 오른쪽 자식]

for _ in range(N):          # N개 노드 읽기
    node,left,right = input().split()       # ['A','B','C']
    binary_tree[node] = [left,right]        # 사전에 노드 정보 삽입

preorder('A')       # 전위 순회
print()
inorder('A')        # 중위 순회
print()
postorder('A')      # 후위 순회