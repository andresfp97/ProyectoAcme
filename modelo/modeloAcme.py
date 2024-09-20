from persistencia.persistenciaAcme import guardarArt

def leerNombre():
    while True:
        try:
            nombre = input("Nombre del Prodcuto? ")
            if len(nombre.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def leerPrecio():
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 4000:
                print(">>> Error.Precio incorrecto")
                continue
            return precio

        except ValueError:
            print("Error. precio invalido.\n")


def leerCantidad():
    while True:
        try:
            cant = int(input("Cantidad en el inventario: "))
            if cant < 0:
                print(">>> Error. en cantidd")
                continue
            return cant

        except ValueError:
            print("Error. cantidad invalido.\n")


def leerDescuento():
    lisDes = []

    while True:
        try:
            descuento = float(input("ingrese el descuento: (-1 para terminar) "))
            if descuento == -1:
                break
            else:
                lisDes.append(descuento)

        except ValueError:
            print("Error. precio invalido.\n")

    return lisDes


def leerCodigo():
    while True:
        try:
            cod = input("Codigo del producto? ")
            if len(cod.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return cod

        except Exception as e:
            print("Error al ingresar el codigo.\n" + e)


def ingProducto(producAcme, arch):

    print("\n\n *** 1. INSERTAR ***")
    cod = leerCodigo()
    if cod not in producAcme:

        nombre= leerNombre()
        precio = leerPrecio()
        cantidad = leerCantidad()
        descuento = leerDescuento()

        datlib = { "nombre": nombre, 
                   "precio": precio,
                   "cantidad": cantidad,
                   "descuento": descuento}

        producAcme[cod] = datlib

        producAcme = dict(sorted(producAcme.items()))

        guardarArt(producAcme, arch)
        
    else:
        print("El codigo ya existe en la libreria.")

    input("Presione cualquier tecla para volver al menu")

    return producAcme


