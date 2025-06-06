# 문제
# 올해 Z대학 컴퓨터공학부에 새로 입학한 민욱이는 학부에 개설된 모든 전공과목을 듣고 졸업하려는 원대한 목표를 세웠다.
# 어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수할 수 있게 되어 있다.
# 공학인증을 포기할 수 없는 불쌍한 민욱이는 선수과목 조건을 반드시 지켜야만 한다.
# 민욱이는 선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수할 수 있는지 궁금해졌다.
# 계산을 편리하게 하기 위해 아래와 같이 조건을 간소화하여 계산하기로 하였다.
#
# 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
# 모든 과목은 매 학기 항상 개설된다.
# 모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계산하는 프로그램을 작성하여라.
#
# 입력
# 첫 번째 줄에 과목의 수 N(1 ≤ N ≤ 1000)과 선수 조건의 수 M(0 ≤ M ≤ 500000)이 주어진다.
# 선수과목 조건은 M개의 줄에 걸쳐 한 줄에 정수 A B 형태로 주어진다.
# A번 과목이 B번 과목의 선수과목이다. A < B인 입력만 주어진다. (1 ≤ A < B ≤ N)
#
# 출력
# 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지를 한 줄에 공백으로 구분하여 출력한다.
#
# 예제 입력 1
# 3 2
# 2 3
# 1 2
# 예제 출력 1
# 1 2 3
# 예제 입력 2
# 6 4
# 1 2
# 1 3
# 2 5
# 4 5
# 예제 출력 2
# 1 2 2 1 3 1
from collections import deque
import sys
input = sys.stdin.readline
v,e = map(int,input().split())
indgree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
result = [0] * (v+1)
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indgree[b]+=1
def topology_sort():
    q = deque()
    for i in range(1,v+1):
        if indgree[i]==0:
            q.append(i)
            result[i] = 1       # 처음 진입 차수가 0인 과목은 1학기 수강
    while q:
        now = q.popleft()
        for adjacent in graph[now]:
            indgree[adjacent] -=1
            if indgree[adjacent]==0:
                q.append(adjacent)
                result[adjacent] = result[now] + 1      # 새롭게 진입 차수가 0이 된 과목은 now 과목 수강 학기 + 1
topology_sort()
for i in range(1,v+1):
    print(result[i],end=' ')