#!/usr/bin/env python3
from random import randint
from brain_games.games.game_logic import start_game


"""
Описание игры «Простое ли число?»:

Суть игры состоит в следующем:

- Пользователю будет показано случайное число,
и ему нужно будет определить, является ли это число простым или нет.
Пользователю будет предложено ввести "yes", если число простое,
или "no", если число не простое.

- Если пользователь даст неверный ответ, игра будет завершена,
и ему будет выведено сообщение:
"'yes' is the wrong answer ;(. The correct answer was 'no'.
Let's try again, (имя пользователя)!"

- Любой некорректный ввод также будет считаться ошибкой,
например, введение "n" будет равносильно неправильному ответу.

- В случае, если пользователь введёт верный ответ, игра будет продолжена,
и ему будет выведено сообщение "Correct!".

- Для успешного прохождения игры пользователю необходимо
правильно ответить на три вопроса подряд.

- После успешного завершения игры будет выведено сообщение
"Congratulations, (имя пользователя)".

- Здесь будет следующая часть кода для реализации игры...
"""


# Игра «Простое ли число?»
def main():
    start_game('Answer "yes" if given number is prime. Otherwise answer "no".',
               game_logic)


# Возвращает случайное число и правильный ответ
def game_logic() -> tuple[str, str]:
    number = randint(0, 100)
    if number < 2:
        return str(number), 'no'
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return str(number), 'no'
        divider += 1
    return str(number), 'yes'


# def game_logic() -> tuple[str, str]:  # Альтернативное решение
#     number = randint(0, 100)
#     dividend = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             dividend.append(i)
#     if len(dividend) == 2:
#         return str(number), 'yes'
#     return str(number), 'no'
