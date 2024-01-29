#!/usr/bin/env python3
from random import randint
import prompt


"""
Описание игры "Проверка на чётность":

Суть игры состоит в следующем:

- Пользователю будет показано случайное число,
и ему нужно будет определить, является ли это число чётным или нечётным.
Пользователю будет предложено ввести "yes", если число чётное,
или "no", если число нечётное.

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


def welcome_user() -> str:   # Приветствие пользователя
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user.capitalize()}!')
    return name_user.capitalize()


# Инструкция для пользователя
def question_user() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


# Возвращает случайное число и правильный ответ
def game_logic() -> tuple[str, str]:
    number = randint(0, 100)
    if number % 2 == 0:
        return str(number), 'yes'
    return str(number), 'no'


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
