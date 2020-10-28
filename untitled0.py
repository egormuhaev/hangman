import os
import random as rd

def hungman(word):
    wrong = 0
    stages = ["",
              "________",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       /\        ",
              "|                 "]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False   
    while wrong < len(stages):
        print("\n")
        message = "Введите букву: "
        char = input(message)
        if char in reletters:
            cin = reletters.index(char)
            board[cin] = char
            reletters[cin] = "@"
            print(("".join(board)))
        else:
            wrong += 1
            print(("".join(board)))
            e = wrong + 1
            print("\n".join(stages[0 : e]))
        if "_" not in board:
            print("Вы выиграли!!! Было загадано слово: " + ("".join(board)))
            win = True
            break
        
    if not win:
        print("".join(stages[0 : wrong]))
        print("Вы проиграли. Было загадано слово: {} ".format(word))
   
file_word = open("lib_x.txt", "r")
x = file_word.read()
word_list = x.split(";")
count = len(word_list)
word = word_list[rd.randint(0,(count-1))]
print("Добро пожаловать на казнь!!!")
print("Количество букв в загаданом слове: " + str(len(word)))
print("Объяснение: ")

hungman(word)

    
    
