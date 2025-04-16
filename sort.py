# array = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(len(array)):     # i = 0,1,2,...,len(array) - 1
#     min_index = i   # 가장 작은 원소의 인덱스
#     for j in range(i+1,len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
# print(array)
# 선택 정렬
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# N + (N - 1) + (N - 2) + ... + 2
# ========> (N^2 + N - 2) / 2
# ========> O(N^2)
#
#=================================================================
# array = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(1,len(array)):
#     for j in range(i, 0, -1):   # j = i,(i-1),(i-2),...,1
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1],array[j]
#         else:
#             break
# print(array)
# 삽입 정렬
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# O(N^2)
# 최선의 경우(거의 정렬된 상태) : O(N)
#
#================================================================
# array = [5,7,9,0,3,1,6,2,4,8]
#
# def quick_sort(array):
#     if len(array)<=1:   # 대상 배열 크기가 1이하이면 종료
#         return array
#     pivot = array[0]    # 피벗은 첫번째 원소
#     tail = array[1:]    # 피벗을 제외한 리스트
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#     # 분할 후 왼쪽 그룹과 오른쪽 그룹을 각각 정렬한 후 합쳐서 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
# print(quick_sort(array))
# 퀵 정렬
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#========================================================================
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# count = [0]*(max(array)+1)
# for i in range(len(array)):
#     count[array[i]] += 1    # 각 데이터 인덱스의 계수 1증가
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')
# 계수 정렬
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
# O(N + K)
# 중복 데이터가 여러 개일 때 효과적이나 메모리 낭비가 심함
#
#============================================================