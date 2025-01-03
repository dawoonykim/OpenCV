# 프로그래머스 - 가위 바위 보

def win(rsp):
    rsp_list = {"2": "0", "0": "5", "5": "2"}

    return "".join(rsp_list[i] for i in rsp)


def solution(rsp):
    return win(rsp)


print(solution("2"))
print(solution("205"))
