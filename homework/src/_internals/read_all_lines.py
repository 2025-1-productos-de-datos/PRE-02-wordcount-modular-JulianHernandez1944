import os


def read_all_lines(input_folder):
    all_lines = []
    input_file_list = os.listdir(
        input_folder
    )  # lista de archivos en el directorio de entrada
    for filename in input_file_list:
        file_path = os.path.join(
            input_folder, filename
        )  # une la ruta del directorio con el nombre del archivo
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines
