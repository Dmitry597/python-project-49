#!/usr/bin/env python3
from random import randint
from brain_games.games.game_logic import start_game


"""
Описание игры: «Наибольший общий делитель (НОД)»
Суть игры в следующем:

- Пользователю показывается два случайных числа, например, 25 50.

- Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

- Если пользователь даст неверный ответ, игра будет завершена,
и ему будет выведено сообщение:
"'1' is the wrong answer ;(. The correct answer was '25'.
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


# Игра «Наибольший общий делитель (НОД)»
def main():
    start_game('Find the greatest common divisor of given numbers.',
               game_logic)


# Возвращает случайные два числа и правильный ответ
def game_logic() -> tuple[str, str]:
    common_divisor = []
    number = [randint(1, 100), randint(1, 100)]
    string = f'{number[0]} {number[1]}'
    for divider in range(1, min(number) + 1):
        if number[0] % divider == 0 and number[1] % divider == 0:
            common_divisor.append(divider)
    return string, str(max(common_divisor))
