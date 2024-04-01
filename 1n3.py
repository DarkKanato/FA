# Задание 3 Урока 1

import logging
import argparse

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def count_matching_numbers(ticket, lottery):
    if len(ticket) != 10 or len(lottery) != 10:
        logging.error("Каждый список должен содержать ровно 10 чисел.")
        return
    count = 0
    for number in ticket:
        if number in lottery:
            count += 1
    logging.info(f'Количество совпадающих чисел: {count}')
    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Определение количества совпадающих чисел между двумя списками.")
    parser.add_argument('ticket', nargs=10, type=int, help="Лотерейный билет - список из 10 чисел.")
    parser.add_argument('lottery', nargs=10, type=int, help="Список чисел, выпавших в лотерею - список из 10 чисел.")
    args = parser.parse_args()

    # Проверка на уникальность чисел в списках
    if len(set(args.ticket)) != 10 or len(set(args.lottery)) != 10:
        logging.error("Числа в каждом списке должны быть уникальными.")
    else:
        count_matching_numbers(args.ticket, args.lottery)
