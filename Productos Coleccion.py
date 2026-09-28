def agregarProducto(tienda, producto, precio):
    tienda[producto] = precio
    return tienda

def mostrarProductos(tienda):
    for producto, precio in tienda.items():
        print(producto, ":", precio)

def buscarProducto(tienda, producto):
    if producto in tienda:
        return tienda[producto]
    else:
        return None

def eliminarProducto(tienda, producto):
    if producto in tienda:
        del tienda[producto]
        return True
    else:
        return False

def calcularTotal(tienda):
    return sum(tienda.values())

if __name__ == "__main__":
    
    tienda = {}

    
    agregarProducto(tienda, "Arroz", 1.5)
    agregarProducto(tienda, "Azucar", 1.2)
    agregarProducto(tienda, "Leche", 0.9)
    agregarProducto(tienda, "Aceite", 3.5)
    agregarProducto(tienda, "Pan", 0.3)

    
    print("Productos de la tienda:")
    mostrarProductos(tienda)

    
    precio_leche = buscarProducto(tienda, "Leche")
    print("Precio de la leche:", precio_leche)

    precio_atun = buscarProducto(tienda, "Atun")
    print("Precio del atun:", precio_atun)

    
    resultado_eliminar = eliminarProducto(tienda, "Pan")
    print("¿Se elimino el pan?", resultado_eliminar)

    
    print("Productos despues de eliminar:")
    mostrarProductos(tienda)

    
    total_productos = calcularTotal(tienda)
    print("Total de los productos:", total_productos)