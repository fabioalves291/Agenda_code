from datetime import datetime, timedelta
from controllers.default import *
from controllers.tarefas.tarefas import *


if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in materiageral:
                datainicial     = datetime.now()
                print(materia,"iniciou às",datainicial.now())
                input("Enter quando terminar:")
                datafinal       = datetime.now()
                print("Finalizado",materia["materia"],"às",datafinal)
                tempodeestudo   =   datafinal - datainicial
                
                print("Estudo de",tempodeestudo,"\n")
                adicionartempo(materia,tempodeestudo.total_seconds())
                #adicionarpositionmateria(materia)
                print("Estudo de",tempodeestudo,"\n")
                break
            #print("oi")
            #adicionarposition((tarefas))
        #print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta = input(":").lower()
        None if resposta=="sim" or resposta=="" else print("saindo...")

