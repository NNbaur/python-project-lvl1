from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while True:
        flag = True
        number1 = randint(1, 101)
        for i in range(2, number1):
            if number1 % i == 0:
                flag = False
        print(f'Question: {number1}')
        answer = input()
        print(f'Your answer: {answer}')
        if flag:
            if answer == 'yes':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'yes'")
                print(f"Let's try again, {name}!")
                break
        elif not flag:
            if answer == 'no':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'no'")
                print(f"Let's try again, {name}")
                break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
