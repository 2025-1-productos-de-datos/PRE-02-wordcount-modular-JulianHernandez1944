# obtain a list of files in the input directory
import os

from homework.src.write_count_words import write_count_words


def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in os.listdir("data/input/"):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(
                lines
            )  # extend() agrega los elementos de la lista lines a la lista all_lines
    return all_lines


def main():

    input_file_list = os.listdir("data/input/")
    # all_lines = read_all_lines()
    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_count_words(counter)


if __name__ == "__main__":
    main()  # hace la llamada a la funcion main
