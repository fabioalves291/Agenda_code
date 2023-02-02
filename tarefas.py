from datetime import datetime
from tarefas.tarefas import *
from controllers import *

if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in materiageral:
                data = (datetime.now())
                horadeinicio = datetime.now().time()
                print(materia,horadeinicio)
                input("Enter quando terminar")
                datafinal = datetime.now()
                print("finalizado",materia,"às",datafinal.time())
                tempoestudado = None
                print(datafinal)
                break
        print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta =input(":").lower()
        print("") if resposta=="sim" or resposta=="" else exit

