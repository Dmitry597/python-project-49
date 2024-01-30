#!/usr/bin/env python3
from random import randint
from brain_games.games.game_logic import start_game


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


# Игра «Арифметическая прогрессия»
def main():
    start_game('What number is missing in the progression?',
               game_logic)


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
