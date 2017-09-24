#! Переворот строки
def str_turn(str):
    out = ''
    for x in str:
        out = x + out
    return out


print(str_turn('hello world!'))