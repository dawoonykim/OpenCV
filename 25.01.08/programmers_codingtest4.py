# 프로그래머스 - 배열 두배 만들기

def solution(numbers):
    answer = [i*2 for i in numbers]
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))
