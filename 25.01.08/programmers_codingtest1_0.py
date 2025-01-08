# 프로그래머스 - 최빈값 구하기

import collections


def solution(array):
    count = collections.Counter(array)
    return count.most_common(1)[0][1]
    



print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
