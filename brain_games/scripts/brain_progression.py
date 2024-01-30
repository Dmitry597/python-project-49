#!/usr/bin/env python3
from random import randint
import prompt


""""
Описание игры: «Арифметическая прогрессия»
Суть игры в следующем:

- Пользователю показывается ряд чисел, который образует
арифметическую прогрессию, заменив любое из чисел двумя точками.

- Игрок должен определить это число.

- Рекомендуемая длина прогрессии – 10 чисел.
Длина может генерироваться случайным образом,
но должна содержать не менее пяти чисел.

- Позиция спрятанного элемента каждый раз изменяется —
выбирается случайным образом.

- Если пользователь даст неверный ответ, игра будет завершена,
и ему будет выведено сообщение:
"'1' is the wrong answer ;(. The correct answer was '15'.
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
    print('What number is missing in the progression?')


# Возвращает случайные два числа и правильный ответ
def game_logic() -> tuple[str, str]:
    progression = []
    step_progres = randint(2, 5)
    start_progres = randint(1, 25)
    while len(progression) < 10:
        progression.append(start_progres)
        start_progres += step_progres
    index_random = randint(0, 9)
    secret_number = progression.pop(index_random)
    progression.insert(index_random, '..')
    return ' '.join(map(str, progression)), str(secret_number)


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
