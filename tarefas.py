from datetime import datetime, timedelta
import importlib

from controllers.default import *
import controllers.tarefas.dictarefas as dictarefas


def adicionartempomateria():
    importlib.reload(dictarefas)
    #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
    tarefas = dictarefas.defdictarefas()
    for materiageralchave, materiageralvalor in tarefas.items():
        for materiachave, materiavalor in tarefas[materiageralchave].items():
            datainicial     = datetime.now()
            print(materiavalor["materia"],"iniciou às",datainicial.now())
            print("tempo estudado:",(int((int(materiavalor["time"]))/3600)),"horas e",int((int(materiavalor["time"])%3600)/60),"minutos")
            input("Enter quando terminar:")
            datafinal       = datetime.now()
            print("Finalizado","às",datafinal)
            tempodeestudo   =   datafinal - datainicial
            print("Estudou",tempodeestudo,"\n")
            tempoestudseg   = int(tempodeestudo.total_seconds())
            adicionartempo(materiavalor,tempoestudseg,materiachave,materiageralchave)
            break