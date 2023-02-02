from datetime import datetime
from tarefas.tarefas import *
from controllers import *

if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in materiageral:
                datainicial = datetime.now()
                print(materia,"iniciou às",datainicial.time())
                input("Enter quando terminar:")
                datafinal = datetime.now()
                print("finalizado",materia,"às",datafinal.time())
                print("estudo de",datafinal-datainicial,"\n")
                tempoestudado = None
                break
        print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta = input(":").lower()
        None if resposta=="sim" or resposta=="" else print("saindo..."),exit()

