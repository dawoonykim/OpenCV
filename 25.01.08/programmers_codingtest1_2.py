# 프로그래머스 - 최빈값 구하기

def solution(array):
    while len(array):
        for i, a in enumerate(set(array)):
            array.remove(a)
            print(a)
        if i == 0:
            return a
    return -1


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
