
from random import randint, choice
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('What is the result of the expression?')
    count = 0
    while True:
        number1 = randint(0, 101)
        number2 = randint(0, 101)
        operator = choice(['*', '+', '-'])
        if operator == '*':
            answer = number1 * number2
        elif operator == '+':
            answer = number1 + number2
        else:
            answer = number1 - number2
        print(f'Question: {number1} {operator} {number2}')
        uranswer = int(input())
        print(f'Your answer: {uranswer}')
        if answer == uranswer:
            print('Correct!')
            count += 1
        else:
            print(f"'{uranswer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
