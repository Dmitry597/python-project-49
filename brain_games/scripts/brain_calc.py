#!/usr/bin/env python3
from random import randint, choice
import prompt


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


def welcome_user() -> str:  # Приветствие пользователя
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user.capitalize()}!')
    return name_user.capitalize()


# Инструкция для пользователя
def question_user() -> None:
    print('What is the result of the expression?')


# Возвращает случайные два числа и правильный ответ
def game_logic() -> tuple[str, str]:
    operation = choice(['+', '-', '*'])
    number = [randint(1, 25), randint(1, 25)]
    string = f'{number[0]} {operation} {number[1]}'
    if operation == '+':
        return string, str(number[0] + number[1])
    elif operation == '-':
        return string, str(number[0] - number[1])
    else:
        return string, str(number[0] * number[1])


# Проверка корректного ответа пользователя
def correct_answer(answer: str, correct: str) -> bool:
    if answer == correct:
        return True
    return False


# Функционал игры
def main():
    name_user = welcome_user()
    question_user()
    count_answer = 0
    while count_answer < 3:
        check_answer = game_logic()
        print(f'Question: {check_answer[0]}')
        answer = input('Your answer: ')
        if not correct_answer(answer, check_answer[1]):
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{check_answer[1]}'.\nLet's try again, {name_user}!")
            return

        print('Correct!')
        count_answer += 1

    print(f'Congratulations, {name_user}!')
