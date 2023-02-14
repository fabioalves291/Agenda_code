from datetime import datetime, timedelta
from controllers.default import *
#from controllers.tarefas.tarefas import *
from controllers.tarefas.dictarefas import *


if __name__ == "__main__":
    while True:
        for materiageral in tarefas:
            for materia in tarefas[materiageral].values():
                datainicial     = datetime.now()
                print(materiageral,materia["tipo"])
                print(materia["materia"],"iniciou às",datainicial.now())
                print("tempo estudado:",materia["time"])
                input("Enter quando terminar:")
                datafinal       = datetime.now()
                print("Finalizado",materia["materia"],"às",datafinal)
                tempodeestudo   =   datafinal - datainicial
                print("Estudou",tempodeestudo,"\n")
                
                adicionartempo(materia,tempodeestudo.total_seconds())
                #adicionarpositionmateria(materia)
    
                break
            #print("oi")
            #adicionarposition((tarefas))
        #print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
        resposta = input(":").lower()
        None if resposta=="sim" or resposta=="" else print("saindo...")

