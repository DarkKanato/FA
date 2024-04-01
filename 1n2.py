# Задание 2 Урока 1
import math
import logging
import argparse

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_prime_number(num):
    if num <= 1:
        logging.error('Число должно быть больше 1 и меньше 100000')
        return False
    elif num > 100000:
        logging.error('Число должно быть больше 1 и меньше 100000')
        return False
    elif num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main(num):
    if is_prime_number(num):
        logging.info(f'Число {num} является простым.')
    else:
        logging.info(f'Число {num} не является простым.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Определение простого числа.")
    parser.add_argument('num', type=int, help="Введите натуральное число для анализа.")
    args = parser.parse_args()

    main(args.num)
