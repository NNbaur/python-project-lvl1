from random import randint
import prompt


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while True:
        flag = True
        number1 = randint(1, 101)
        flag = isPrime(number1)
        print(f'Question: {number1}')
        answer = input()
        print(f'Your answer: {answer}')
        if flag and answer == 'no':
            print(f"'{answer}' is wrong answer ;(. "
                  "Correct answer was 'yes'")
            print(f"Let's try again, {name}!")
            break
        elif not flag and answer == 'yes':
            print(f"'{answer}' is wrong answer ;(. "
                  "Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            break
        count += 1
        print('Correct!')
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
