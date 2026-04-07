def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input()
    minusculas = (nombre.lower())
    print(f"Contiene a: {'a' in minusculas}")
    print(f"Contiene e: {'e' in minusculas}")
    print(f"Contiene i: {'i' in minusculas}")
    print(f"Contiene o: {'o' in minusculas}")
    print(f"Contiene u: {'u' in minusculas}")
