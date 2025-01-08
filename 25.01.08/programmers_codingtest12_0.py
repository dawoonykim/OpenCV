# 프로그래머스 - 중복된 숫자 개수

def solution(array, n):
    answer = 0
    for num in array:
        if num == n:
            answer += 1
    return answer


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))
