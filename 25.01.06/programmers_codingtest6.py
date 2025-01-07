# 프로그래머스 - 직각삼각형 출력하기

n = int(input())
# print(n)
answer = "\""
for i in range(1, n+1):
    answer += "*"*i
    if i < n:
        answer += "\n"
answer += "\""

print(answer)
