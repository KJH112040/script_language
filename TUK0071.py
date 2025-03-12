# N,M = map(str,input().split())
# output=[['.' for _ in range(len(N))]for _ in range(len(M))]
#
# for i in range(len(M)):
#     c = N.find(M[i])
#     if c != -1:
#         for j in range(len(N)):
#             output[i][j] = N[j]
#         for j in range(len(M))
#             output[j][c] = M[j]
#         break
#

#===============교수님 코드===================
[A,B]=input().split()
M = [['.']*len(A) for _ in range(len(B))]

for c in range(len(A)):
    r = B.find(A[c])    #A단어의 c번째 문자를 B단어에서 찾는다.
    if r != -1:         #찾았으면 r행 c열에서 중볻
        break
for i in range(len(A)): #r행에 A단어를 넣는다.
    M[r][i] = A[i]
for i in range(len(B)): #c열에 B단어를 넣는다.
    M[i][c] = B[i]

for i in range(len(B)): #행의 갯수
    print(''.join(M[i]))