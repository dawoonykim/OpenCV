# 프로그래머스 - 특정 문자 제거하기

def solution(my_string, letter):
    answer = ''
    # s_list = list(my_string)

    change_str = my_string.replace(letter, "")
    print(change_str)
    return answer


print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
