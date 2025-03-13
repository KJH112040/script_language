def solution(dartResult):
    answer = 0              # 최종 점수
    # number = 0              # 현재 기회의 숫자
    # current=0               # 현재 기회의 계산된 점수
    # previous =0             # 이전 기회의 계산된 점수
    # for c in dartResult:    # 문자 하나씩 검사
    #     if '0'<=c<='9':     # 점수는 0점~10점
    #         if c=='0' and number==1:
    #             number=10
    #         else:
    #             number=int(c)
    #     elif c=='S':
    #         previous = current
    #         current = number**1
    #         answer += current
    #     elif c == 'D':
    #         previous = current
    #         current = number ** 2
    #         answer += current
    #     elif c == 'T':
    #         previous = current
    #         current = number ** 3
    #         answer += current
    #     elif c=='*':
    #         answer-=(previous+current)
    #         previous*=2
    #         current*=2
    #         answer+=(previous+current)
    #     elif c=='#':
    #         answer -= current
    #         current *= -1
    #         answer+=current

    turn = []
    count = 0
    for i in range(len(dartResult)):
        if dartResult[i]>='0' and dartResult[i]<='9':
            if dartResult[i]=='1' and dartResult[i+1] == '0':
                turn.append(int(dartResult[i])*10)
            else:
                turn.append(int(dartResult[i]))
        elif dartResult[i]=='*':
            if count !=0:
                turn[count-1],turn[count]=turn[count-1]*2,turn[count]*2
            else:
                turn[count]=turn[count]*2
            count += 1
        elif dartResult[i]=='#':
            turn[count]=turn[count]*-1
            count+=1
        else:
            if dartResult[i]=='D':
                turn[count] = turn[count]**2
            elif dartResult[i]=='T':
                turn[count] = turn[count]**3

            if i!=len(dartResult)-1 and dartResult[i + 1] != '*' and dartResult[i + 1] != '#':
                count += 1
    for i in range(3):
        answer+=turn[i]

    return answer

dr = input()
print(solution(dr))