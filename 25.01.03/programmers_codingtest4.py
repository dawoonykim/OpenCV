# 프로그래머스 - 개미 군단

def cal(hp):
    count = 0
    a_g = 5
    a_s = 3
    a_w = 1
    rest_hp = hp
    # print(rest_hp)

    while rest_hp != 0:
        if rest_hp >= a_g:
            count += 1
            rest_hp -= a_g
            print(rest_hp)
        elif rest_hp >= a_s:
            count += 1
            rest_hp -= a_s
            print(rest_hp)
        elif hp >= a_w:
            count += 1
            rest_hp -= a_w
            print(rest_hp)

    return count


def solution(hp):

    return cal(hp)


print(solution(23))
print(solution(24))
# print(solution(999))
