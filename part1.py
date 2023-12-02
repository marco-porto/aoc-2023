import re
import logging

from file_reader import FileReader

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    output = 0

    with FileReader("input.txt") as file:
        words = file.readlines()

    for word in words:
        word = re.sub("[^0-9.]", "", word)
        output += int(word[0] + word[len(word) - 1])

    logging.info(output)


