# 프로그래머스 - 피자 나눠 먹기(3)

import math
def cal(slice, n):
    # print(f"1 : {int(n/slice)}")
    # print(f"2 : {int(slice/n+0.5)}")
    return math.ceil(n/slice)


def solution(slice, n):

    return cal(slice, n)


print(solution(7, 10))
print(solution(4, 12))
