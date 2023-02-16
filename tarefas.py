from datetime import datetime, timedelta
from controllers.default import *
from tarefas.dictarefas import tarefas

while True:
    for materiageralchave, materiageralvalor in tarefas.items():
        print("retornando primeiro for")
        for materiachave, materiavalor in tarefas[materiageralchave].items():
            print(materiachave,materiavalor)
            print()
            datainicial     = datetime.now()
            #print(materiageralchave,materia["tipo"])
            print(materiavalor["materia"],"iniciou às",datainicial.now())
            print("tempo estudado:",materiavalor["time"])
            input("Enter quando terminar:")
            datafinal       = datetime.now()
            print("Finalizado","às",datafinal)
            tempodeestudo   =   datafinal - datainicial
            print("Estudou",tempodeestudo,"\n")
            tempoestudseg   = int(tempodeestudo.total_seconds())
            adicionartempo(materiavalor,tempoestudseg,materiachave,materiageralchave)
            #adicionarpositionmateria(materia)
            break

        #print("oi")
        #adicionarposition((tarefas))
    #print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
    resposta = input("finalizado:").lower()
    exit()


