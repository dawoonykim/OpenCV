# 프로그래머스 - 머쓱이보다 키 큰 사람

def solution(array, height):
    answer = []
    for i in array:
        if i > height:
            answer.append(i)
    return len(answer)


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))
