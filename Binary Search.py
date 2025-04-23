# # 이분탐색 재귀 함수
# def binary_search(array,target,start,end):
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid]>target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
# ...
# # 이진탐색 반복문
# def binary_search(array,target,start,end):
#     while start<=end:
#         mid = (start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# # n 원소 개수, target 찾고자 하는 값
# n, target = map(int,input().split())
# # 정렬된 전체 원소를 입력 받는다
# array = list(map(int,input().split()))
# # 이진 탐색 수행결과 출력
# result = binary_search(array,target,0,n-1)
# if result==None:
#     print('원소가 존재하지 않는다')
# else:
#     print(result+1)
#
#==================================================================================
# 특정 범위 데이터 개수 구하기
# from bisect import bisect_left,bisect_right
#
# def count_by_range(a,left,right):
#     return bisect_right(a,right) - bisect_left(a,left)
#
# a = [1,2,3,3,3,3,4,4,8,9]
# # 값이 4인 데이터 개수
# print(count_by_range(a,4,4))
# # 값이 [-1,3]범위 데이터 개수
# print(count_by_range(a,-1,3))
#
#==================================================================================
# n 떡의 개수, m 손님이 요청한 떡길이
n,m = map(int,input().split())
# 떡 배열
array = list(map(int,input().split()))
start = 0
end = 1000000000
# 조건을 만족하는 절단기 최대 높이
result = 0
# 이분 탐색
while start<= end:
    mid = (start+end)//2
    total = 0       # 자르고 남은 떡길이 변수
    for x in array:
        if x > mid:
            total += x - mid
    if total< m:        # 조건을 만족하지 않는다.
        end = mid - 1
    else:               # 조건을 만족
        result = mid    # 정답 후보
        start = mid + 1
print(result)