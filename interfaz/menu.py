def menuAcme():

    while True:
      print(">>>> MENU ACME <<<<")
      print("="*60)
      print("1- Agregar producto")  
      print("2- Buscar producto")
      print("3- Listar productos")  
      print("4- Listar producto con menos inventario")  
      print("5- Listar producto con mayor porcentaje de descuento")
      print("6- Listar producto con menor precio con descuento")  
      print("7- Listar producto con mayor precio en inventario")  
      print("8- Salir") 
      print(">> Escoja una opción (1-8)?", end="")
      print("="*60)

      try:
            opcion = int(input())
            if opcion < 1 or opcion > 8:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
      except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")