# 프로그래머스 - 옷가게 할인 받기

def discount(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    else:
        return price


def solution(price):
    return discount(price)


print(solution(150000))
print(solution(580000))
print(solution(300000))
