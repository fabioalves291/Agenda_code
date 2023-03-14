from tarefasfuncao import adicionartempomateria
from controllers.default import *
import logging
import os 

try:

    if __name__ == "__main__":
        while True:
            input("iniciando...")
            input("deseja estudar alguma materia especifica?\n>>")
            print(verificarmaterinotset(),'ciclos finalizados')
            setarmateriazerada(verificarmaterinotset())
            adicionartempomateria()
            input("finalizado:")
except  Exception as e :
    print(e)
    logging.basicConfig(filename="log/log.log",level=logging.DEBUG,filemode="a")
    logger = logging.getLogger()
    logger.exception(str(e))

    

        