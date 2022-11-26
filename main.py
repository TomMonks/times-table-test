import random


def print_questions(num1, num2):
    for a, b in zip(num1, num2):
        print(f'{a} X {b} = ')

def main(n_questions, random_seed=None):
    random.seed(random_seed)

    num_1 = [random.randint(2, 12) for _ in range(n_questions)]
    num_2 = [random.randint(2, 12) for _ in range(n_questions)]

    answers = [a * b for a, b in zip(num_1, num_2)]

    print_questions(num_1, num_2)


if __name__ == '__main__':
    main(15)

        