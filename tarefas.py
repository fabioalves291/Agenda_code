from datetime import datetime
from controllers.default import *
from controllers.tarefas.tarefas import *


if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in materiageral:
                datainicial     = datetime.now()
                print(materia,"iniciou às",datainicial.time())
                input("Enter quando terminar:")
                datafinal       = datetime.now()
                print("Finalizado",materia["materia"],"às",datafinal.time())
                tempodeestudo   =   datafinal - datainicial
                adicionartempo(materia,tempodeestudo)
                #adicionarpositionmateria(materia)
                #print("Estudo de",tempodeestudo,"\n")
                break
            #print("oi")
            #adicionarposition((tarefas))
        #print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta = input(":").lower()
        None if resposta=="sim" or resposta=="" else print("saindo...")

