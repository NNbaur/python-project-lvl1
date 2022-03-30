from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('What number is missing in the progression?')
    count = 0
    while True:
        progression = []
        while len(progression) <= 5:
            num1 = randint(1, 101)
            num2 = randint(1, 101)
            step = randint(1, 101)
            progression = [str(i) for i in range(min(num1, num2),
                           max(num1, num2), step)]
        a = randint(0, len(progression) - 1)
        answer = progression.pop(a)
        progression.insert(a, '..')
        print('Question:', *progression)
        uranswer = input()
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
