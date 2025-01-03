# 프로그래머스 - 구슬을 나누는 경우의 수

def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result


def solution(balls, share):
    answer = int(factorial(balls)/(factorial(balls-share)*factorial(share)))
    return answer


print(solution(3, 2))
print(solution(5, 3))
