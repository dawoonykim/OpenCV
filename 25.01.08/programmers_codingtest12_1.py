# 프로그래머스 - 중복된 숫자 개수

from collections import Counter
def solution(array, n):
    count = Counter(array)
    return count[n]


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))
