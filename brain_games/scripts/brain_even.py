#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():   # Приветствие пользователя
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')
    return name.capitalize()


name_user = ''  # Имя пользователя


def game_instructions():  # Инструкция для пользователя
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_number(number):  # Проверка: четное или нечетное число
    even = ''
    if number % 2 == 0:
        even = 'yes'
    else:
        even = 'no'
    return even


def user_answer():  # Ответ пользователя
    answer = input('Your answer: ')
    return answer


correct = 'Correct!'   # Переменная для сравнения правильного ответа


def check_answer(reply, chance):  # Проверка корректного ответа пользователя
    check = ''
    if reply == 'yes' and chance == 'yes':
        check = correct
    elif reply == 'no' and chance == 'no':
        check = correct
    else:
        check = f"'{reply}' is wrong answer ;(. Correct answer was 'no'.\n" \
                f"Let's try again, {name_user}!"
    return check


def game():
    count = 0
    while count < 3:
        random_number = randint(1, 100)
        print('Question: ', random_number)
        response_user = user_answer()
        if check_answer(response_user, even_number(random_number)) == correct:
            count += 1
            if count == 3:
                print(f'Congratulations, {name_user}!')
        else:
            print(f"'{response_user}' is wrong answer ;(."
                  f"Correct answer was 'no'.\nLet's try again, {name_user}!")
            break


def main():
    global name_user
    global correct
    name_user = welcome_user()
    game_instructions()
    game()


if __name__ == '_main_':
    main()
