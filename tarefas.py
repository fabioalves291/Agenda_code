from datetime import datetime, timedelta
import importlib
from controllers.default import *
import controllers.tarefas.dictarefas as dictarefas
import contestudando.contadorestudando  as contestudando


def adicionartempomateria():
    importlib.reload(dictarefas)
    
    #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
    
    tarefas = dictarefas.defdictarefas()
    cont=0
    for materiageralchave, materiageralvalor in tarefas.items():
        passouparaproximamateria    =    True
        importlib.reload(contestudando)
        print(cont == contestudando.contadorestudando(),cont,contestudando.contadorestudando())
        if cont == contestudando.contadorestudando():
            for materiachave, materiavalor in tarefas[materiageralchave].items():
                if adicionarpositionmateria(materiavalor):
                    datainicial     = datetime.now()
                    print(materiavalor["materia"],"iniciou às",datainicial.now())
                    print("tempo estudado:",(int((int(materiavalor["time"]))/3600)),"horas e",int((float(materiavalor["time"])%3600)*60),"minutos")
                    input("Enter quando terminar:")
                    datafinal       = datetime.now()
                    print("Finalizado","às",datafinal)
                    tempodeestudo   =   datafinal - datainicial
                    print("Estudou",tempodeestudo,"\n")
                    tempoestudseg   = int(tempodeestudo.total_seconds())
                    adicionartempo(materiavalor,tempoestudseg,materiachave,materiageralchave)
                    file = open("contestudando/contadorestudando.py","w")
                    file.write(fr"def contadorestudando():contmateriaestudando = {cont+1}; return contmateriaestudando ")
                    file.close()
                    input(":estudar proxima materia do ciclo?")
                    break
        cont+=1
    file = open("contestudando/contadorestudando.py","w")
    file.write(fr"def contadorestudando():contmateriaestudando = {0}; return contmateriaestudando ")
    file.close()
    
    
        
        