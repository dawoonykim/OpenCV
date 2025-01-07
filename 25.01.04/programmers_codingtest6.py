# 프로그래머스 - 양꼬치

def solution(n, k):
    answer = 0
    flag = True
    while flag:
        if n % 10 == 0:
            k -= 1
        else:
            flag = False
    answer = 12000*n+2000*k
    return answer


print(solution(10, 3))
print(solution(64, 6))
