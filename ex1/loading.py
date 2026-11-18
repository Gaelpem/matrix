import importlib
import sys
def  verif_module(dict_modules : dict[str, str]) -> list[str]:
    paquets_manquants = []
    for cle, value in dict_modules.items():
        try:
            module = importlib.import_module(cle)
        except ModuleNotFoundError: # si le module n'est pas trouvé on le rajoute dans le nouveau tab
            paquets_manquants.append(cle)# si un paquet n'est pas installé, le programme l'ajoute à paquets_manquants
        else:
            print(f"[OK] {cle} ({module.__version__}) : -{value}")
    return paquets_manquants

def show_install_instructions() -> None:
    print("\nMissing dependencies detected!")
    print("Installation with pip:")
    print("pip install -r requirements.txt")
    print("python3 loading.py")
    print("Install with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")
   
def analyse() -> None:
    import numpy
    import pandas
    import matplotlib.pyplot
    print("\nAnalyzing Matrix data...")
    s = numpy.random.uniform(0, 100, 1000)
    print(f"Processing {len(s)} data points...")
    data = pandas.DataFrame({"name_colonne":s})
    print(data.describe())
    print("Generating visualization...\n")
    matplotlib.pyplot.hist(data["name_colonne"])
    name_img = "matrix_analysis.png"
    matplotlib.pyplot.savefig(name_img)
    print("Analysis complete!")
    print(f"Resultat saved to: {name_img}")

def show_environment() -> None:
    print(f"Environment : {sys.prefix}")

def main() -> None:
    show_environment()
    print("\nChecking dependencies:")
    paquet_dicctionnaire = {"pandas": "Data manipulation ready",
                            "numpy" : "Numerical computation ready",
                            "matplotlib" : "Visualization"}
    module_verifs_manquants = verif_module(paquet_dicctionnaire)
    if module_verifs_manquants: #si il ya des paquets
        for paquet_manquant in module_verifs_manquants:
            print(f"[MISSING] {paquet_manquant}")
        show_install_instructions()# Elle affiche à l'utilisateur comment installer les paquets,avec pip ou Poetry
        sys.exit(1)
    analyse()

print("LOADING STATUS: Loading prgrams...")
if __name__ == "__main__":
    main()
