# 프로그래머스 - 최빈값 구하기

def solution(array):
    count = [0]*(max(array)+1)

    for i in array:
        count[i] += 1

    m = 0

    for c in count:
        if c == max(count):
            m += 1
    if m >= 2:
        return -1
    return count.index(max(count))


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
