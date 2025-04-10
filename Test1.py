# Description A
#
# 정왕동에 새로운 극장이 문을 열었습니다.
#
# 극장의 한 줄에는 N개의 좌석이 있습니다.
#
# 인접한 좌석 사이에는 하나의 컵 홀더가 있으며 열의 양쪽 끝에 두 개의 추가 컵 홀더가 있습니다.
#
# 그러나 한 쌍의 러브 시트 사이에는 컵 홀더가 없습니다.
#
# 당신의 임무는 어떤 행의 좌석을 설명하는 일련의 문자가 주어지고 모든 좌석이 찼다고 가정할 때
#
# 좌석 바로 옆에 있는 컵 홀더에 컵을 놓을 수 있는 최대 사람 수를 찾는 것입니다.
#
# 좌석 표시의 'S'는 일반석, 'L'은 러브시트를 의미합니다. 러브시트는 항상 두개씩 쌍으로 제공됩니다.
#
# 예를 들어서 좌석 시퀀스가'SLLLLSSLL' 로 주어지고, 컵홀더를 '*' 로 표시하면 다음과 같이 좌석을 표시할 수 있습니다.
#
# * S * L L * L L * S * S * L L *
#
# 따라서 이 예에서는 최대 7명이 바로 옆에 있는 컵 홀더에 컵을 넣을 수 있습니다.
#
#
# Input
#
# 첫 번째 줄에는 좌석 수인 정수 N(1 ≤ N ≤ 50)이 포함됩니다.
#
# 다음 줄에는 좌석 시퀀스를 설명하는 N개 문자 'L' 또는 'S'가 포함됩니다.
#
# 3
# SSS
#
# Output
#
# 컵을 바로 옆에 있는 컵 홀더에 놓을 수 있는 최대 인원수를 출력 합니다.
#
# 3
#
# Hint greedy
#
# N = int(input())
# seat = list(input())
# cup = []
# answer = 0
# L_cnt = 0
#
# for i in range(N):
#     if i == 0:
#         cup.append('*')
#         answer +=1
#     if seat[i] == 'S':
#         cup.append('S')
#         cup.append('*')
#         answer += 1
#     elif seat[i] == 'L':
#         if L_cnt == 1:
#             cup.append('L')
#             cup.append('*')
#             answer+=1
#             L_cnt = 0
#         else:
#             cup.append('L')
#             L_cnt+=1
#
# print(min(N,answer))
#
#
# 스도쿠는 논리 기반의 조합 숫자 배치 퍼즐입니다.
#
# 목표는 9×9 격자판에 1부터 9까지의 숫자를 채우는 것입니다.
#
# 스도쿠 문제는 다음의 규칙이 있습니다.
#
# 각 행에는 1부터 9까지의 각 숫자가 정확히 한 번만 포함됩니다.
# 각 열에는 1부터 9까지의 각 숫자가 정확히 한 번만 포함됩니다.
# 9개의 3 × 3 하위 격자 각각에는 1부터 9까지의 각 숫자가 정확히 한 번만 포함됩니다.
# 아직 완료되지 않은 스도쿠 격자판에 대해 실수가 있는지 확인하세요.
#
# 다음과 같은 스도쿠 예제가 주어진다면 이 예제는 실수가 없습니다.
#
#
# 또 다른 다음의 예제는 9번째 열에 5가 두번 나타나고, 오른쪽 아래 3x3 서브격자판에서도 5가 두번 나타나므로 실수가 있습니다.
#
#
# 마지막 아래 예제를 보면 2번째 열에 2가 두번 나타나고, 7번째 열에는 6이 두번 나타나므로 실수가 있습니다.
#
#
# Input
#
# 첫번째 줄에는 스도쿠 문제 개수 n(1<=n<=100) 가 나타납니다.
#
# 그리고 그 다음줄부터 n개의스도쿠 격자판이 나타납니다.
#
# '|', '-' 및 '+' 문자는 3 × 3 서브 격자판의 틀을 구성합니다.
#
# '.' 문자는 빈 셀을 나타냅니다.
#
# 입력의 다른 모든 문자는 '1'에서 '9'까지의 숫자입니다.
#
#
# Output
#
# n줄에 걸쳐서 스도쿠가 실수가 없으면 대문자 Y, 실수가 있으면 대문자 N을 출력하시오.
#
# n = int(input())
# board = [[list(input()) for _ in range(13)] for _ in range(n)]
# answer = ['Y' for _ in range(n)]
#
# for i in range(n):
#     end = False
#     r3c3 = [[] for _ in range(9)]
#     r9 = [[] for _ in range(9)]
#     c9 = [[] for _ in range(9)]
#     for j in range(1,12):
#         if end:
#             break
#         if j == 4 or j == 8:
#             continue
#         for k in range(1,12):
#             if k == 4 or k == 8:
#                 continue
#             if board[i][j][k] == '.':
#                 continue
#             else:
#                 if board[i][j][k] in r9[j]:
#                     answer[i] = 'N'
#                     end = True
#                     break
#                 else:
#                     r9[j].append(board[i][j][k])
#
#                 if board[i][k][j] in c9[j]:
#                     answer[i] = 'N'
#                     end = True
#                     break
#                 else:
#                     c9[j].append(board[i][k][j])
#
#                 if 1<=j<=3:
#                     if 1<=k<=3:
#                         if board[i][j][k]in r3c3[0]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[0].append(board[i][j][k])
#                     elif 5<=k<=7:
#                         if board[i][j][k]in r3c3[1]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[1].append(board[i][j][k])
#                     elif 9<=k<=11:
#                         if board[i][j][k]in r3c3[2]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[2].append(board[i][j][k])
#                 elif 5<=j<=7:
#                     if 1<=k<=3:
#                         if board[i][j][k]in r3c3[3]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[3].append(board[i][j][k])
#                     elif 5<=k<=7:
#                         if board[i][j][k]in r3c3[4]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[4].append(board[i][j][k])
#                     elif 9<=k<=11:
#                         if board[i][j][k]in r3c3[5]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[5].append(board[i][j][k])
#                 elif 9<=j<=11:
#                     if 1<=k<=3:
#                         if board[i][j][k]in r3c3[6]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[6].append(board[i][j][k])
#                     elif 5<=k<=7:
#                         if board[i][j][k]in r3c3[7]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[7].append(board[i][j][k])
#                     elif 9<=k<=11:
#                         if board[i][j][k]in r3c3[8]:
#                             answer[i] = 'N'
#                             end = True
#                             break
#                         else:
#                             r3c3[8].append(board[i][j][k])
#
# for c in answer:
#     print(c)
# Description
#
# 아름답고 읽기 쉬운 코드를 작성하는 국제 대회인 Kod가 올해 처음으로 개최됩니다!
#
# 대회에는 1부터 n까지의 숫자가 표시된 n명의 참가자가 참여하며, 각 참가자는 코드를 작성했습니다.
#
# 그들의 코드는 컴퓨터 과학자 협회에 의해 평가됩니다. 협회는 회장과 협회 회원으로 구성됩니다.
#
# 평가는 회장과 회원들의 평가로 이루어 집니다.
#
#
#
# 회장 평가:
# 회장은 (그의 생각에) 가장 아름다운 코드부터 가장 덜 아름다운 코드까지 순위를 매길 것입니다.
#
# 첫 번째 코드에는 n 포인트가 부여되고, 이후의 각 코드에는이전 점수보다 1점 적게 부여됩니다.
#
#
#
# 회원 평가
# 협회의 각 회원은 자신이 가장 아름답다고 생각하는 코드에 투표합니다.
#
# 협회의 각 회원이 투표한 후, 코드는 협회 회원으로부터 받은 투표 수에 따라 내림차순으로 순위가 매겨집니다.
#
# 첫 번째 코드(가장 많은 표를 얻은 코드)에는 n 포인트가 부여되고, 이후의 각 코드는 이전 코드보다 1포인트 적게 부여됩니다.
#
#
#
# 총점
# 각 코드별 총점수는 회장이 부여한 점수와 협회 회원이 부여한 점수의 합과 같습니다.
#
#
#
# 귀하의 작업은 총점에 따라 내림차순으로 참가자 코드 순서를 인쇄하는 것입니다.
#
# 동일한 점수를 가진 참가자 코드가 생길 경우에는 협회 회원으로부터 더 많은 점수를 획득한 참가자 코드가 더 높은 순위를 차지합니다.
#
#
# Input
#
# 첫 번째 줄에는 참가자 수인 정수 n(1 ≤ n ≤ 50)이 포함됩니다.
#
# 두 번째 줄에는 n개의 정수 ai(1 ≤ ai ≤ n)가 포함되어 있습니다. 여기서 i번째 정수는 회장이 i번째 순위를 매긴 참가자 코드의 번호가 나타냅니다. 즉 첫번째 나타나는 참가자 코드 번호가 1등입니다.
#
# 회장의 순위는 가장 아름다운 것부터 가장 덜 아름다운 것 순으로 주어지며, 1부터 n까지의 모든 숫자는 정확히 한 번씩 포함합니다.
#
# 세 번째 줄에는 n개의 정수 bi(0 ≤ bi ≤ 200)가 포함되어 있습니다. 여기서 i번째 정수는 i번째 코드가 협회 회원으로부터 받은 투표 수를 나타냅니다. 즉 1번 참가자 코드의 투표수가 첫번째 나타납니다.
#
# 동일한 수의 표를 얻은 코드는 없습니다.
#
#
# Output
#
# n줄에 걸쳐서 총점에 따라서 참가자 코드의 순위를 내림차순으로 출력합니다.
#
# 각 줄은 "[순위]. Kod[숫자] ([총점])" 형식이어야 합니다. 여기서 [순위]는 참가자 코드의 순위이고, [숫자]는 해당 순위의 참가자 코드 번호입니다.
#
# 앞에 0이 붙는 두 자리 형식이며, [총점]은 참가자 코드가 획득한 총점입니다.
#
# 예를 들어, 참가자 코드 3번이 총점 12점으로 1위를 차지하면 첫번째 줄은 다음과 같습니다.
#
# n = int(input())
# ai = list(map(int,input().split()))
# bi = list(map(int,input().split()))
# p = []
# answer = []
#
# for i in range(n):
#     p.append((i+1,bi[i]))
#
# p.sort(reverse=True,key=lambda x:(x[1],x[0]))
# bscore = n
#
# for i in range(n):
#     ascore = n - ai.index(p[i][0])
#     answer.append((p[i][0], ascore+bscore))
#     bscore-=1
#
# answer.sort(reverse=True,key=lambda x:(x[1],x[0]))
#
# # 점수가 똑같을 때 회원 점수로,
#
# for i in range(n):
#     if 0<answer[i][0] <10:
#         print(f'{i+1}. Kod0{answer[i][0]} ({answer[i][1]})')
#     else:
#         print(f'{i+1}. Kod{answer[i][0]} ({answer[i][1]})')