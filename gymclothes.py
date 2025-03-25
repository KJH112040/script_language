def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    for r in _reserve:
        f = r -1
        b = r+1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))