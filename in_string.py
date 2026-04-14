def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input()
    minusculas = (nombre.lower())
    if "a" in minusculas:
        print(f"Contiene a: True")
    elif "a" not in minusculas:
        print(f"Contiene a: False")
    if "e" in minusculas:
        print(f"Contiene e: True")
    elif "e" not in minusculas:
        print(f"Contiene e: False")
    if "i" in minusculas:
            print(f"Contiene i: True")
    elif "i" not in minusculas:
            print(f"Contiene i: False")
    if "o" in minusculas:
        print(f"Contiene o: True")
    elif "o" not in minusculas:
        print(f"Contiene o: False")
    if "u" in minusculas:
        print(f"Contiene u: True")
    elif "u" not in minusculas:
        print(f"Contiene u: False")
