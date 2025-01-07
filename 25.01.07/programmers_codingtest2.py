# 프로그래머스 - 배열의 평균값

def cal(numbers):

    sum_all = sum(numbers)

    return sum_all/len(numbers)


def solution(numbers):
    return cal(numbers)


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
