import os  # os interactua con el sistema operativo


def test_migracion():
    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")

    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value
    assert (
        results.get("computational", 0) == "3"
    )  # verifica que la palabra computational aparezca 3 veces sino asigna 0
    assert (
        results.get("analytics", 0) == "5"
    )  # verifica que la palabra science aparezca 2 veces sino asigna 0
