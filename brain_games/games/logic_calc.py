#!/usr/bin/env python3
from random import randint, choice
from brain_games.games.game_logic import start_game


""""
Описание игры: «Калькулятор»
Суть игры в следующем:

- Пользователю показывается случайное математическое выражение,
например, "35 + 16" которое нужно вычислить и записать правильный ответ.

- Операции, как и числа, выбираются случайным образом

- Если пользователь даст неверный ответ, игра будет завершена,
и ему будет выведено сообщение:
"'145' is the wrong answer ;(. The correct answer was '175'.
Let's try again, (имя пользователя)!"

- Любой некорректный ввод также будет считаться ошибкой,
например, введение "n" будет равносильно неправильному ответу.

- В случае, если пользователь введёт верный ответ, игра будет продолжена,
и ему будет выведено сообщение "Correct!".

- Для успешного прохождения игры пользователю необходимо
правильно ответить на три вопроса подряд.

- После успешного завершения игры будет выведено сообщение
"Congratulations, (имя пользователя)".

Здесь будет следующая часть кода для реализации игры...
"""


# Игра «Калькулятор»
def main():
    start_game('What is the result of the expression?',
               game_logic)


# Возвращает случайные два числа и правильный ответ
def game_logic() -> tuple[str, str]:
    operation = choice(['+', '-', '*'])
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    string = f'{number1} {operation} {number2}'
    if operation == '+':
        return string, str(number1 + number2)
    elif operation == '-':
        return string, str(number1 - number2)
    else:
        return string, str(number1 * number2)
