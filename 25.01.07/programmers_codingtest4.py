# 프로그래머스 - 피자 나눠 먹기(2)

import math


def cal(n):
    return (abs(n*6)//math.gcd(n, 6))//6


def solution(n):

    return cal(n)


print(solution(6))
print(solution(10))
print(solution(4))
