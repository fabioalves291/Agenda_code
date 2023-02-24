from datetime import datetime, timedelta
import importlib
from controllers.default import *
import controllers.tarefas.dictarefas as dictarefas
from contestudando.contestudando import contestudando 
def adicionartempomateria():
    importlib.reload(dictarefas)
    
    #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
    
    tarefas = dictarefas.defdictarefas()
    cont=0
    for materiageralchave, materiageralvalor in tarefas.items():
        passouparaproximamateria    =    True
        importlib.reload(contestudando)
        print(cont == contestudando(),cont,contestudando())
        if cont == contestudando():
            for materiachave, materiavalor in tarefas[materiageralchave].items():
                if adicionarpositionmateria(materiavalor):
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
                    file = open("contestudando/contestudando.py","w")
                    file.write(fr"def contestudando():contmateriaestudando = {cont}; return contmateriaestudando ")
                    file.close()
                    input("escrevendo cont")
        cont+=1
        
        