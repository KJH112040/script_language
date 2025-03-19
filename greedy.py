#예시
# n=1260
# count =0
# array=[500,100,50,10]
# for coin in array:
#     count += n//coin
#     print(coin,'동전', n//coin,'개')
#     n%=coin
# print(count)

#예시
# n,k=map(int,input().split())
# result=0
# while True:
#     #n이 k로 나누어 떨어지는 수가 될때 까지 -1
#     target = (n//k)*k
#     result +=(n - target)
#     print('n=', n, ' target=', target, ' result=', result)
#     n= target
#     #n이 k보다 작을 때 (더 이상 나눌 수 없을 때)
#     if n<k:
#         break
#     #k로 나누기
#     result+=1
#     n//=k
# #마지막 남은 수에 대해서 1씩 빼기
# result+=(n-1)
# print(result)

#예시
# data = input() #숫자 문자열 입력 '02987'
# #첫번째 문자를 숫자로 변경
# result = int(data[0])
# for i in range(1, len(data)):
#     # 두수 중에서 하나라도 0,1인 경우라면 덧셈
#     num = int(data[i])
#     if result<=1 or num<=1:
#         result+=num
#     else:
#         result*=num
# print(result)

#에시
#5
#2 3 1 2 2
# n = int(input())
# data=list(map(int,input().split()))
# data.sort() #공포도 오름차순 정렬
# result =0   #그룹의 총 수
# count = 0   #현재 그룹의 모험가 수
# for i in data:  # 공포도 낮은 애부터
#     count+=1    #현재 그룹에 모험가 한명추가
#     if count>=i:    #현재 그룹 포함수가 현재 공초도 이상이면
#         result+=1   #그룹화 시키고
#         count =0    #초기화
# print(result)

#예시
# n = int(input())
# r,c = 1,1
# plans=input().split()#['R','R','R','U','D','D']
# #L,R,U,D 방향 벡터
# # dr=[0,0,-1,1]
# # dc=[-1,1,0,0]
# d = [(0,-1),(0,1),(-1,0),(1,0)]
# move_types=['L','R','U','D']
# #이동 계획 하나씩 확인
# for plan in plans:
#     #이동 후 좌표 구하기
#     i = move_types.index(plan) #plan을 찾아서 인덱스 반환
#     nr = r+d[i][0]
#     nc = c + d[i][1]
#     if 1<=nr<=n and 1<=nc<=n:
#         r,c,=nr,nc
# print(r,c)

#예시
#N입력
#00시00분00초 부터 N시59분59초까지 중에서 3이 들어간 시각의 수
# N = int(input())
# count=0
# for h in range(N+1):    #h =1,2,...,N
#     for m in range(60): #m =1,2,...,59
#         for s in range(60): #s = 1,2,...,59
#             if '3' in str(h)+str(m)+str(s):
#                 count+=1
# print(count)

#예시
#현재 나이트 위치 입력 'a1','c5'
# data = input()
# r = int(data[1])
# c = ord(data[0])-ord('a')+1 #a:h ->1:8
# #8가지 방향 벡터
# steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
# #8가지 각 위치로 이동 가능한지 확인
# result =0
# for step in steps:
#     nr = r + step[0]
#     nc = c+step[1]
#     if 1 <= nr <=8 and 1<=nc<=8:
#         result+=1
# print(result)

#예시
data = input()  #알파벳 대문자와 숫자로 이루어진 문자열
result=[]   #알파벳 문자들을 갖는 리스트
value = 0   #숫자의 합

#문자를 하나씩 확인
for x in data:
    if x.isalpha(): #알파벳이면
        result.append(x)    #result = ['K','A','Z',...
    else:   #숫자이면
        value += int(x)
result.sort()   #오름차순 정렬
if value != 0:  # 숫자가 존재하면
    result.append(str(value))
#AKZ19
print(''.join(result))