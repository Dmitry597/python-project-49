#!/usr/bin/env python3
from random import randint
from random import choice
import prompt


""""
Описание игры: «Калькулятор»
Суть игры в следующем: 

- Пользователю показывается случайное математическое выражение,
например, "35 + 16" которое нужно вычислить и записать правильный ответ.

- Операции, как и числа, выбираются случайным образом

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

Здесь будет следующая часть кода для реализации игры...
"""


def welcome_user() -> str:  # Приветствие пользователя
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user.capitalize()}!')
    return name_user.capitalize()


def question_calc() -> None:
    print('What is the result of the expression?')


def expression_check() -> tuple[str, str]:
    operation = choice(['+', '-', '*'])
    number = [randint(1, 25), randint(1, 25)]
    string = f'{number[0]} {operation} {number[1]}'
    if operation == '+':
        return string, str(number[0] + number[1])
    elif operation == '-':
        return string, str(number[0] - number[1])
    else:
        return string, str(number[0] * number[1])


def correct_answer(name_user: str, correct: str) -> bool:
    answer = input('Your answer: ')
    if answer == correct:
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'."
              f"\nLet's try again, {name_user}!")


# Функционал игры
def main():
    name_user = welcome_user()
    question_calc()
    count_answer = 0
    while count_answer < 3:
        check_answer = expression_check()
        print(f'Question: {check_answer[0]}')
        if not correct_answer(name_user, check_answer[1]):
            return

        print('Correct!')
        count_answer += 1

    print(f'Congratulations, {name_user}!')
