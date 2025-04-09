# 재귀 DFS
def DFS(port,path,graph,ports,nTickets):
    i = ports.index(port)   # port 인덱스를 ports에서 구함
    for j in range(len(ports)):     # j = 0,1,...,N-1, port 공항에서 갈 수 있는 알파벳이 빠른 공항을 찾는다
        if graph[i][j]> 0:  # i->j 티켓이 존재하면
            graph[i][j]-= 1 # 해당 경로 티켓 1 감소
            nTickets -= 1
            port = ports[j] # 시작 공항을 j인덱스 공항으로 변경
            # 재귀호출 ICA->AAA->BBB->CCC ... 계속 자식을 호출
            (answer,nTickets) = DFS(port,path + [port], graph, ports, nTickets)
            if nTickets == 0:
                return (answer,nTickets)
            else:       # ICN-->AAA 로 시작하면 전체 순회가 불가하나 ICN-->CCC로 시작할 경우 전체 순회가 가능하면
                graph[i][j]+=1
                nTickets +=1
    return (path,nTickets)

def solution(tickets):
    answer = []
    ports = set()   # 공항 집합
    for a,b in tickets:
        ports.add(a)
        ports.add(b)
    ports = list(ports) # list로 형변환
    ports.sort()        # 알파벳 오름차순 정렬

    N = len(ports)  # 공항 개수
    graph = [[0]*N for _ in range(N)]
    for a,b in tickets:
        i = ports.index(a)      # ports 리스트에서 a공항 인덱스 구함
        j = ports.index(b)      # ports 리스트에서 b공항 인덱스 구함
        graph[i][j] += 1        # 동일한 경로 티켓이 여러 장 있을 수 있다.

    nTickets = len(tickets)     # tickets 개수
    port = 'ICN'        # 시작 공항
    path = ['ICN']      # 여행 경로
    (answer,nTickets)=DFS(port,path,graph,ports,nTickets)

    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

# STEP 1 tickets을 조회해서 중복되지 않는 공항 리스트를 알파벳 순서로 생성
# STEP 2 tickets과 ports를 이용해서 graph[][] int형 2차원 배열 구성
# STEP 3 ICN에서 시작해서 DFS로 모든 티켓을 소진하도록 탐색