from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while True:
        num1 = randint(1, 101)
        num2 = randint(1, 101)
        for i in range(1, min(num1, num2) + 1):
            if num1 % i == num2 % i == 0:
                answer = i
        print(f'Question: {num1} {num2}')
        uranswer = input()
        print(f'Your answer: {uranswer}')
        if str(answer) == uranswer:
            print('Correct!')
            count += 1
        else:
            print(f"'{uranswer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
