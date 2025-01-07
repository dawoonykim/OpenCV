# 프로그래머스 - 외계행성의 나이

def change_age(age):
    age_list = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e",
                "5": "f", "6": "g", "7": "h", "8": "i", "9": "j"}

    split_age = list(str(age))
    # print(split_age)
    answer = []
    for i in split_age:
        answer.append(age_list[i])

    return "".join(answer)


def solution(age):

    return change_age(age)


print(solution(23))
print(solution(51))
print(solution(100))
