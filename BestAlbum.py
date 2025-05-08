# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
#   genres[i]는 고유번호가 i인 노래의 장르입니다.
#   plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
#   genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
#   장르 종류는 100개 미만입니다.
#   장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
#   모든 장르는 재생된 횟수가 다릅니다.
#
# 입출력 예
#   genres	                                            plays	                        return
#   ["classic", "pop", "classic", "classic", "pop"]	    [500, 600, 150, 800, 2500]	    [4, 1, 3, 0]
#
# 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
#   고유 번호 3: 800회 재생
#   고유 번호 0: 500회 재생
#   고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
#   고유 번호 4: 2,500회 재생
#   고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
#   장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.
def solution(genres, plays):
    answer = []
    D = {}      # 딕셔너리 key:value = 장르:[총재생횟수, (1등 고유번호, 횟수), (2등 고유번호, 횟수)]
    for i in range(len(genres)):        # i = 0,1,2,...,len(genres)-1 고유번호
        genre, play = genres[i],plays[i]    # i 고유번호의 장르와 재생 횟수
        if genre in D:      # 해당 장르가 딕셔너리에 존재하면 갱신
            D[genre][0]+=play   # 총 재생횟수 누적
            if D[genre][1][1] < play:   # i번 재생횟수가 딕셔너리 1등 횟수보다 크다면
                D[genre][1],D[genre][2] = (i, play),D[genre][1]
            elif D[genre][2][1]<play:   # i번 재생횟수가 딕셔너리 2등 획수보다 크다면
                D[genre][2] = (i,play)

        else:       # 해당 장르가 딕셔너리에 존재하지 않는다면 삽입
            D[genre] = [play,(i,play),(-1,0)]
    #print(D)
    #{'classic': [1450, (3, 800), (0, 500)], 'pop': [3100, (4, 2500), (1, 600)]}
    G = []      # 딕셔너리의 (key,value) 원소로 갖는 리스트
    for genre, value in D.items():
        G.append((genre,value[0]))
    #print(G)
    #[('classic', 1450), ('pop', 3100)]
    G.sort(key=lambda x:x[1],reverse=True)      # 총 재생횟수 기준 내림차순 정렬
    #print(G)
    #[('pop', 3100), ('classic', 1450)]
    for i in range(len(G)):
        genre = G[i][0]         # 해당 장르
        answer.append(D[genre][1][0])       # 해당 장르의 1등 고유번호 추가
        if D[genre][2][0] != -1:
            answer.append(D[genre][2][0])   # 해당 장르의 2등 고유번호가 있다면 추가

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))