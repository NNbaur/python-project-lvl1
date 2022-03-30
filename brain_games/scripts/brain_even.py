from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 0
    while True:
        number = randint(0, 101)
        print(f'Question: {number}')
        answer = input()
        print(f'Your answer: {answer}')
        if number % 2 == 0:
            if answer == 'yes':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'yes'")
                print(f"Let's try again, {name}!")
                break
        elif number % 2 != 0:
            if answer == 'no':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'no'")
                print(f"Let's try again, {name}!")
                break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
