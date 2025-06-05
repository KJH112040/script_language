# 두 수의 합
# 시간 제한	메모리 제한	제출	    정답	    맞힌 사람	정답 비율
# 1 초	    128 MB	    79208	28683	20789	    34.608%
# 문제
# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
# ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수열의 크기 n이 주어진다.
# 다음 줄에는 수열에 포함되는 수가 주어진다.
# 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)
#
# 출력
# 문제의 조건을 만족하는 쌍의 개수를 출력한다.
#
# 예제 입력 1
# 9
# 5 12 7 10 9 1 2 3 11
# 13
# 예제 출력 1
# 3
n = int(input())
data = list(map(int,input().split()))
x = int(input())
data.sort()     # 오름차순 정렬
# data = [1, 2, 3, 5, 7, 9, 10, 11, 12]

# 투 포인터
count = 0
end = 1     # end는 start보다 크다
# start를 차례로 이동 시키면서
for start in range(n-1):    # start = 0, 1, ..., n-2 (end보다 작아야 하기 때문)
    if start == end:    # 두 포인터가 같다면 end 1 증가
        end += 1
    # if data[start] + data[end] < x, end를 가능한 오른쪽으로 이동
    while data[start]+data[end]< x and end < n - 1:
        end += 1
    # if data[start] + data[end] > x, end를 가능한 왼쪽으로 이동
    while data[start]+data[end] > x and end > start + 1:
        end -= 1
    if data[start]+data[end] == x:
        count += 1
print(count)