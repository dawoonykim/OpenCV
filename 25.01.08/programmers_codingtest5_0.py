# 프로그래머스 - 분수의 덧셈
import math


def solution(numer1, denom1, numer2, denom2):
    lcm = int(denom1*denom2/math.gcd(denom1, denom2))

    print(lcm)
    numer_total = (numer1*(lcm//denom1))+(numer2*(lcm//denom2))
    denom_total = lcm

    answer = [numer_total, denom_total]
    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
