import sys
import site
import os.path

def is_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False
def off_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment")
    print("The machines can see everything you install\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows ")
    print("\nThen ruen this program again")

def in_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install package without affecting")
    print("the global system")
    liste_package = site.getsitepackages()
    print("\nPackage installation path:")
    print(liste_package[0])

def main() -> None:
    if is_venv():
        in_venv()
    else:
        off_venv()

if __name__ == "__main__":
    main()