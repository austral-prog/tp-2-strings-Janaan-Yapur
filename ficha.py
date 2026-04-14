def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    # ficha.py

    # Inputs
    nombre = input().strip().title()
    email = input().strip().lower()
    nota1 = int(input().strip())
    nota2 = int(input().strip())
    nota3 = int(input().strip())

    # Procesamiento del nombre
    pos_espacio = nombre.find(" ")

    nombre_pila = nombre[:pos_espacio]
    apellido = nombre[pos_espacio + 1:]

    iniciales = nombre_pila[0] + apellido[0]
    usuario = f"{apellido.lower()}.{nombre_pila.lower()}"

    # Email
    email_valido = "@" in email
    pos_arroba = email.find("@")
    dominio = email[pos_arroba + 1:] if pos_arroba != -1 else ""

    # Otros datos de strings
    nombre_archivo = nombre.replace(" ", "_")
    cantidad_a = nombre.lower().count("a")
    codigo_secreto = nombre[::-1].upper()

    # Notas
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)
