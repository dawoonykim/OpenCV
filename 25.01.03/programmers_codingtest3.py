# 프로그래머스 - 모스부호(1)

def morse(letter):
    l_list = letter.split()
    moth_list = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m",
                 "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}
    return "".join(moth_list[i] for i in l_list)


def solution(letter):

    return morse(letter)


print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))
