import re
import logging

from file_reader import FileReader

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    output = 0

    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    with FileReader("input_short.txt") as file:
        words = file.readlines()

    for word in words:
        for key, value in numbers.items():
            r = word.find(key)

            if r != -1:
                logging.info(f"{key} - len:{len(key)} - {word} - {r} - {word[r:r + len(key)]}")

    logging.info(output)


