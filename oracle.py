import os
import dotenv
import sys
import os.path

def loaded_configuration() -> dict[str, str | None]:
    new_dictionnaire : dict [str, str | None] = {}
    dotenv.load_dotenv() # transformation chaque ligne NOM=VALEUR en variable d'environnement
    liste_env = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL","ZION_ENDPOINT"]
    for name in liste_env:
        new_dictionnaire[name] = os.getenv(name)
    return new_dictionnaire

# elle verifie la configuration et signale les variables qui n'ont pas de valeur.
def configuration_manquantes(dict_config : dict[str, str | None])  -> list[str]:
    list_vide = []
    for cle,valeur in dict_config.items():
        if valeur == None:
            list_vide.append(cle)
            print(f"WARNING : {cle}")
    return list_vide

def affichage_config(confi_dict : dict[str, str | None], mode : str) -> None:
    print("ORACLE STATUS: Reading the Matrix")
    print("\nConfiguration loaded: ")
    print(f"MODE: {mode}")
    database_mode = confi_dict.get("DATABASE_URL")
    mode_api = confi_dict.get("API_KEY")
    log_mode = confi_dict.get("LOG_LEVEL")
    zion_api = confi_dict.get("ZION_ENDPOINT")
    
    if database_mode and "localhost" in database_mode:
        print("Database: Connected to local instance")
    elif database_mode:
        print("Database: Connected to local instance")
    else:
        print("Database : No configured")
    
    if mode_api:
        print("API Access: Authenticated")
    else:
        print("API Access : No configured")
        
    if log_mode:
        print(f"Log Level: {log_mode}")
    else:
        print("Log Level: No configured")
    
    if zion_api:
        print("Zion Network: Online")
    else:
        print("Zion Network: No configured")
        
def controle_configuration(listes_manquantes : list[str], confi_dict : dict[str, str | None]) -> None:
    print("\nEnvironment security check:")
    api_key = confi_dict.get("API_KEY")
    exist_env = os.path.exists(".env.example") 
    chemin = __file__
    with open(chemin) as file:
        result = file.read()
    if api_key and api_key in result:
        print("[WARNING] API key found in source code")
    else:
        print("[OK] No hardecoded secrets detected")
    if listes_manquantes:
        print("[WARNING].env file is incomplete")
    else:
        print("[OK].env file properly configured")
    if exist_env:
        print("[OK] Production overrides available")
    else:
        print("[WARNING].env.example not found")

def main() -> None:
    dict_envi = loaded_configuration()
    manquantes = configuration_manquantes(dict_envi)
    mode = dict_envi.get("MATRIX_MODE")
    if mode is None:
        mode = "development"
    if manquantes and mode == "production":
        print("Erreur")
        sys.exit(1)
    affichage_config(dict_envi, mode)
    controle_configuration(manquantes, dict_envi)
  
    print("The Oracle sees all configurations.")

if __name__ == "__main__":
    main()
    