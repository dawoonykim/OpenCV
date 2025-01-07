# 프로그래머스 - 아이스 아메리카노

def solution(money):
    answer = []
    price = 5500

    cups = money//price
    rest = money % price
    # print(cups, rest)
    answer.append(cups)
    answer.append(rest)
    return answer


print(solution(5500))
print(solution(15000))
