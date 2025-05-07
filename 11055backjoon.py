# 문제
# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에
# 합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.
# dp[i] : array[i]를 끝 원소로 갖는 증가하는 부분 수열의 최대 합
# dp[i] 초기값은 array[i] 설정
# dp[i] = max(dp[i],dp[j]+array[i]) if array[j]<array[i] (0<=j<i)
n = int(input())
a = list(map(int,input().split()))
dp = a[:]
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            dp[i] = max(dp[i],dp[j]+a[i])
print(max(dp))