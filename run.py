from tarefas import adicionartempomateria
from controllers.default import *

import os 
if __name__ == "__main__":
    while True:
        input("iniciando:")
        print(verificarmaterinotset(),'ciclos finalizados')
        setarmateriazerada(verificarmaterinotset())
        adicionartempomateria()
        input("finalizado:")
        