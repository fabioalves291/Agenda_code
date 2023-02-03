from datetime import datetime
from controllers import *
from controllers.tarefas.tarefas import *

if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in materiageral:
                datainicial = datetime.now()
                print(materia,"iniciou às",datainicial.time())
                input("Enter quando terminar:")
                datafinal  = datetime.now()
                print("Finalizado",materia,"às",datafinal.time())
                tempodeestudo   =   datafinal-datainicial
                adicionarponto(materia,tempodeestudo)
                print("Estudo de",tempodeestudo,"\n")
                break
        print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta = input(":").lower()
        None if resposta=="sim" or resposta=="" else print("saindo...")

