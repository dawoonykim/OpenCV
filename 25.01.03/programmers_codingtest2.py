# 프로그래머스 - 가위 바위 보

def win(rsp):
    rsp_list = list(rsp)
    result = ""
    for i in rsp_list:
        if i == "2":  # 가위
            result += "0"
        elif i == "0":  # 바위
            result += "5"
        elif i == "5":  # 보
            result += "2"
    return result


def solution(rsp):
    return win(rsp)


print(solution("2"))
print(solution("205"))
