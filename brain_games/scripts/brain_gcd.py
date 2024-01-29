#!/usr/bin/env python3
from random import randint
import prompt


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


def welcome_user() -> str:  # Приветствие пользователя
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user.capitalize()}!')
    return name_user.capitalize()


# Инструкция для пользователя
def question_user() -> None:
    print('Find the greatest common divisor of given numbers.')


# Возвращает случайные два числа и правильный ответ
def game_logic() -> tuple[str, str]:
    common_divisor = []
    number = [randint(1, 100), randint(1, 100)]
    string = f'{number[0]} {number[1]}'
    for divider in range(1, min(number) + 1):
        if number[0] % divider == 0 and number[1] % divider == 0:
            common_divisor += [divider]
    return string, str(max(common_divisor))


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
