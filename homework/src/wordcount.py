# obtain a list of files in the input directory
import os

from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.write_count_words import write_count_words


def main():

    # Leer las líneas_Mover a read_all_lines.py
    all_lines = (
        read_all_lines()
    )  # extend() agrega los elementos de la lista lines a la lista all_lines

    # Procesado de las líneas__ mover a preprocess_lines.py
    all_lines = preprocess_lines(
        all_lines
    )  # strip() elimina los espacios en blanco al principio y al final de la línea

    # Separar las líneas en palabras mover a split_in_words.py
    words = []
    for line in all_lines:
        words.extend(
            word.strip(",.!?") for word in line.split()
        )  # split() divide la línea en palabras y strip() elimina los signos de puntuación

    # conteo mover a count_words.py
    counter = {}
    for word in words:
        counter[word] = (
            counter.get(word, 0) + 1
        )  # get() devuelve el valor de la clave si existe, sino devuelve 0

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_count_words(counter)


if __name__ == "__main__":
    main()
