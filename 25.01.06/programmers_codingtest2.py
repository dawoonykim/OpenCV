# 프로그래머스 - 각도기

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4


print(solution(70))
print(solution(91))
print(solution(180))
