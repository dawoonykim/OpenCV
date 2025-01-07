# 프로그래머스 - 짝수가 싫어요

def cal(n):
    num = []
    for i in range(1, n+1):
        if not i % 2 == 0:
            num.append(i)
    return num


def solution(n):

    return cal(n)


print(solution(10))
print(solution(15))
