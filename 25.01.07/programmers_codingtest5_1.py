# 프로그래머스 - 피자 나눠 먹기(1)

import math


def cal(n):
    return (n-1)//7+1


def solution(n):

    return cal(n)


print(solution(7))
print(solution(1))
print(solution(15))
