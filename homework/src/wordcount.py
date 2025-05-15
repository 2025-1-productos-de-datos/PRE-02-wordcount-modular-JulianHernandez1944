# obtain a list of files in the input directory
import os
import sys

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts


def main():

    if len(sys.argv) != 3:
        print("Usage: python -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]  # directorio de entrada
    output_folder = sys.argv[2]  # directorio de salida

    # Leer las líneas_Mover a read_all_lines.py
    all_lines = read_all_lines(input_folder)

    # Procesado de las líneas__ mover a preprocess_lines.py
    all_lines = preprocess_lines(all_lines)
    # Separar las líneas en palabras mover a split_in_words.py
    words = split_into_words(all_lines)
    # conteo mover a count_words.py
    counter = count_words(words)
    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()
