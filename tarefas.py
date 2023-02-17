from datetime import datetime, timedelta
import importlib

from controllers.default import *
import controllers.tarefas.dictarefas as dictarefas


def adicionartempomateria():
    importlib.reload(dictarefas)
    #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
    tarefas = dictarefas.deftarefas()
    
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
    del tarefas


    #print("oi")
    #adicionarposition((tarefas))
    #print("Ciclo finalizado\ndeseja reiniciar o ciclo?")
    resposta = input("finalizado:").lower()
        


