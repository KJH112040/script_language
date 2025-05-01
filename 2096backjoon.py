# 문제
# N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다.
# 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
#
# 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다.
# 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
# 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다.
# 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.
#
#   | * |   |   |               |   | * |   |               |   |   | * |
#   | o | o | x |               | o | o | o |               | x | o | o |
#
# 별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며,
# 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다.
# 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오.
# 점수는 원룡이가 위치한 곳의 수의 합이다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다.
# 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.
#
# 출력
# 첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.
# 내려가기, 메모리 초과에 주의
# dp_max[r][c] = array[r][c] + max(dp_max[r-1])[c-1],dp_max[r-1][c],dp_max[r-1][c+1])
n = int(input())
dp_max = list(map(int,input().split()))
dp_min = dp_max[:]  # 값복사
for _ in range(n-1):    # n-1 행 더 읽는다.
    array = list(map(int,input().split()))
    p_max = [None] * 3
    p_min = [None] * 3
    for c in range(3):  # c = 0, 1, 2 (열 변수)
        # 왼쪽 위
        if c==0: up_left_max = 0; up_left_min = 1e12
        else:    up_left_max = dp_max[c-1]; up_left_min = dp_min[c-1]
        # 위
        up_max = dp_max[c]
        up_min = dp_min[c]
        # 오른쪽 위
        if c==2: up_right_max = 0; up_right_min = 1e12
        else:    up_right_max = dp_max[c+1]; up_right_min = dp_min[c+1]
        p_max[c] = array[c]+max(up_left_max,up_max,up_right_max)
        p_min[c] = array[c] + min(up_left_min, up_min, up_right_min)
    dp_max = p_max[:]
    dp_min = p_min[:]
print(f'{max(dp_max)} {min(dp_min)}')