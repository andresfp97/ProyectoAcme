from interfaz.menu import menuAcme
from modelo.modeloAcme import ingProducto
from persistencia.persistenciaAcme import cargarArt

producAcme = {}

archivo = "productosAcme.json"
producAcme = cargarArt(archivo)

while True:
    op = menuAcme()

    match op:
        case 1:
            producAcme = ingProducto(producAcme, archivo)
        case 2:
            pass
        case 3:
            print("\n\nGracias por usar el software")
            break