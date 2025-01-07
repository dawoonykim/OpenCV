# 프로그래머스 - 진료 순서 정하기

def answer(emergency):
    length = len(emergency)
    e_list = [0*i for i in range(len(emergency))]
    # print(e_list)

    sort_v = sorted(emergency)[::-1]

    for i in range(1, length+1):
        # print(f"sort_v : {sort_v}")
        index = emergency.index(sort_v[i-1])
        # print(f"index : {index}")
        e_list[index] = i

    return e_list


def solution(emergency):

    return answer(emergency)


print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))
