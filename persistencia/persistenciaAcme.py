import json
from pathlib import Path

def guardarArt(artAcme,  arch):
    with open(arch,"w") as fd:
        json.dump(artAcme, fd)


    
def cargarArt(arch):
    archivo = Path(arch)
    produtAcme = {}
    if archivo.is_file():
        try:
            with open(arch, "r")as fd:
                produtAcme = json.load(fd)
            if not fd.closed:
                fd.close()
        except Exception as e:
            print(">>> error al abrir el archivo. \n",e)
        
    else:
        print(">>> error.el archivo no existe")
        input(">>> Presione cualquier tecla para continuar...")
    
    return produtAcme