# 소수 회문(Palindrome)
# Description
# 주어진 정수와 그 정수를 reverse한 정수가 서로 같으면 그 정수는 회문(Palindrome)이라고 합니다.
# 예를 들어 79197 및 324423은 Palindrome입니다.
#
# 정수 N(1 ≤ N ≤ 1000000)이 하나 주어지고,  M이 소수(prime number)이고 Palindrome이되는 가장 작은 정수M (M ≥ N)을 찾습니다.
# M은 N보다 크거나 같습니다.
# M이 소수(prime number)이므로 M은 1과 M으로만 나누어 떨어져야 합니다.
# 예를 들어, N이 31이면 답 M은 101입니다.
#
# Input
# 하나의 정수 N (1 ≤ N ≤ 1000000) 입력
#
# Output
# 출력은 N보다 크거나 같은 가장 작고 소수 Palindrome을 만족하는 정수 M 출력
#
# Sample Input 1
# 31
# Sample Output 1
# 101
def isPrime(X):
    for i in range(2,int(X**0.5)+1):
        if X % i == 0:
            return False
    return True
N = input()
while True:
    N = str(N)
    if N == N[::-1]:
        N = int(N)
        if isPrime(N):
            print(N)
            break
    N = int(N) + 1

#교수님 코드
def isPalindrome(N):
    return str(N) == str(N)[::-1]
def isPrime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

X = int(input())
while True:
    if isPalindrome(X) and isPrime(X):
        print(X)
        break
    X+=1