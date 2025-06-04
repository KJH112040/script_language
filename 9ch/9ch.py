# def isPrime(X):
#     for i in range(2,int(X**0.5)+1):
#         if X % i == 0:
#             return False
#     if X==1 or X==0:
#         return False
#     return True
#
# print(isPrime(0))
# print(isPrime(1))
# print(isPrime(7))
# print(isPrime(213))
#===================================================
# 에라토스테네스의 체는 빠르다
# n = 1000    # 2부터 1000사이의 모든 수중에서 소수 찾는다.
# # 처음엔 모든 숫가 소수(True)인 것으로 초기화
# array = [True]*(n+1)
# # 에라토스테네스의 체
# # 2부터 n의 제곱근까지 모든 수 확인
# for i in range(2,int(n**0.5)+1):
#     if array[i]:    # i가 소수이면
#         # i를 제외한 i의 배수를 지운다.
#         j = 2
#         while i*j <= n:
#             array[i*j] = False
#             j +=1
# for i in range(2, n+1):
#     if array[i]:
#         print(i,end=' ')
# 다음 주 시험에도 이 에라토스테네스의 체를 활용해야 하는 문제가 나온다.
# 조금 변형해야 하는데 변형해야 하는 문제들은 다 힌트로 주어졌다.
# isPrime으로 하나 하나 판별하면 시간 초과에 걸린다.
#===============================================================
# 특정한 합을 가지는 부분연속수열 찾기
n = 5 # 데이터 개수
m = 5 # 찾고자 하는 부분합
data = [1,2,3,4,5] # 전체 수열
count = 0
interval_sum = 0
end = 0
# start를 차례로 증가시키며 반복
for start in range(n): # start = 0, 1, ... , n-1
    # end를 가능한 만큼 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m이면 count를 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)