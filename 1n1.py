# Задание 1 Урока 1

import logging
import argparse

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError as e:
        logging.error("Все параметры должны быть числами.")
        return

    if a <= 0 or b <= 0 or c <= 0:
        logging.error("Длины сторон должны быть положительными числами.")
    elif a > (b + c) or b > (a + c) or c > (a + b):
        logging.info('Треугольник не существует')
    else:
        logging.info('Треугольник существует')
        if a == b == c:
            logging.info('Треугольник равносторонний')
        elif a == b or a == c or b == c:
            logging.info('Треугольник равнобедренный')
        else:
            logging.info('Треугольник разносторонний')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка существования треугольника и его типа по длинам сторон.")
    parser.add_argument('a', help="Длина стороны a")
    parser.add_argument('b', help="Длина стороны b")
    parser.add_argument('c', help="Длина стороны c")
    args = parser.parse_args()


    try:
        check_triangle(args.a, args.b, args.c)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")