# 프로그래머스 - 순서쌍의 개수
def pair(n):
    num = n
    pair_list = []
    for i in range(1, n+1):
        if num % i == 0:
            pair_list.append([i, int(num/i)])

        # print(pair_list)
    return len(pair_list)

def solution(n):

    return pair(n)


print(solution(20))
print(solution(100))
