# 프로그래머스 - 짝수 더하기

def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer


print(solution(10))
print(solution(4))
