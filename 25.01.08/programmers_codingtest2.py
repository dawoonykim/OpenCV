# 프로그래머스 - 중앙값 구하기

def solution(array):
    answer = sorted(array)

    return answer[int(len(array)/2)]


print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))
