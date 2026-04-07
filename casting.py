def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input())
    print(f"Precio: {precio}")
    descuento = float(input())
    print(f"Descuento: {descuento}")
    cantidad = int(input())
    precio_c_descuento = precio - descuento
    print(f"Precio con descuento: {precio_c_descuento}")
    total = precio_c_descuento * cantidad
    print(f"Total: {total}")  
