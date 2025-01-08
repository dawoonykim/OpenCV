# 프로그래머스 - 분수의 덧셈
import math


def solution(numer1, denom1, numer2, denom2):
    numer_total = numer1*denom2+numer2*denom1
    denom_total = denom1*denom2

    gcd = math.gcd(numer_total, denom_total)
    answer = [numer_total//gcd, denom_total//gcd]
    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
