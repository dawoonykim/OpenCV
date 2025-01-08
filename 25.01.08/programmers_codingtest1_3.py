# 프로그래머스 - 최빈값 구하기

import collections


def solution(array):

    while len(array):
        for i, a in enumerate(set(array)):
            if a in array:
                array.remove(a)
        if i == 0:
            return a
    return -1


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
