# 프로그래머스 - 짝수 홀수 개수

def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    answer.append(even)
    answer.append(odd)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))
