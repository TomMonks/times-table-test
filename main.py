import random

def print_questions(num1, num2):
    number = [i+1 for i in range(len(num1))]
    for q, a, b in zip(number, num1, num2):
        print(f'{q}: {a} X {b} = ')

def print_answers(answers):
    for i in range (len(answers)):
        print(f'{i}: {answers[i]}')

def main(n_questions, random_seed=None):
    random.seed(random_seed)

    num_1 = [random.randint(2, 12) for _ in range(n_questions)]
    num_2 = [random.randint(2, 12) for _ in range(n_questions)]

    answers = [a * b for a, b in zip(num_1, num_2)]

    print_questions(num_1, num_2)
    print_answers(answers)


if __name__ == '__main__':
    main(15)

        