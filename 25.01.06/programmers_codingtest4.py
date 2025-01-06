# 프로그래머스 - 문자 반복 출력하기

def solution(my_string, n):
    answer = ''
    str_list = list(my_string)

    for ch in str_list:
        answer += ch*n
    return answer


print(solution("hello", 3))
