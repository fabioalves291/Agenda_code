from datetime import datetime, timedelta
import importlib
import os.path
from controllers.default import *
import tarefas.dictarefas as dictarefas
import contestudando.contadorestudando as contestudando

def adicionarmateriaespecifica():
    def auxilir(materia):
        #copia da funcao adicionartempomateria()
        importlib.reload(dictarefas)
        #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
        tarefas = dictarefas.defdictarefas()
        cont=1
        for materiageralchave, materiageralvalor in tarefas.items():
            variaveldependetedocontador = False
            passouparaproximamateria    = True
            importlib.reload(contestudando)
            #print(cont == contestudando.contadorestudando(),cont,contestudando.contadorestudando())
            for materiachave, materiavalor in tarefas[materiageralchave].items():
                #print(materiavalor["materia"].lower(),materia.lower())

                if materiavalor["materia"].lower() == materia.lower():
                    datainicial     = datetime.now()
                    print(materiavalor["materia"],"iniciou às",datainicial.now())
                    print("tempo estudado:",(int((int(materiavalor["time"]))/3600)),"horas e",int((float(materiavalor["time"])%3600)/60),"minutos")
                    v = True
                    while v:
                        input("Enter quando terminar\n>>")
                        datafinal       = datetime.now()
                        ve = str(input("tem certeza? você estudou "+str(datafinal - datainicial)+"\n>>"))
                        try:
                            if ve[0] in  " sSyYs":v = False
                        except IndexError:
                            if ve in " SsyY":v =False
                    datafinal       = datetime.now()
                    print("Finalizado","às",datafinal)
                    tempodeestudo   =   datafinal - datainicial
                    print("Estudou",tempodeestudo,"\n")
                    tempoestudseg   = int(tempodeestudo.total_seconds())
                    adicionartempo(materiavalor,tempoestudseg,materiachave,materiageralchave)
                    variaveldependetedocontador = True
                    inputcontinuar = input(">> estudar proxima materia do ciclo?")
                    if inputcontinuar.lower() in"  simyes":
                        pass
                    else: 
                        return False

                    break
            zerarcontarestudando(cont,tarefas,variaveldependetedocontador)        
            cont+=1
        #antes de zerar tem que ver se cont é igual ao maximo
        
        return 0
    materia = input(">> qual materia vc quer estuda?\n>> ")
    auxilir(materia)
    print(">> saindo de materia especifica")
    return 0
def adicionartempomateria():
    importlib.reload(dictarefas)
    
    #!!! registrar esse modulo (importlib.reload) no site e outras alternativas !!!
    
    tarefas = dictarefas.defdictarefas()
    cont=1
    for materiageralchave, materiageralvalor in tarefas.items():
        variaveldependetedocontador = False
        passouparaproximamateria    = True
        importlib.reload(contestudando)
        #print(cont == contestudando.contadorestudando(),cont,contestudando.contadorestudando())

        if cont == contestudando.contadorestudando():
            for materiachave, materiavalor in tarefas[materiageralchave].items():
                if adicionarpositionmateria(materiavalor):
                    datainicial     = datetime.now()
                    print(materiavalor["materia"],"iniciou às",datainicial.now())
                    print("tempo estudado:",(int((int(materiavalor["time"]))/3600)),"horas e",int((float(materiavalor["time"])%3600)/60),"minutos")
                    v = True
                    while v:
                        input("Enter quando terminar\n>>")
                        datafinal       = datetime.now()
                        ve = str(input("tem certeza? você estudou "+str(datafinal - datainicial)+"\n>>"))
                        try:
                            if ve[0] in  " sSyYs":v = False
                        except IndexError:
                            if ve in " SsyY":v =False
                    datafinal       = datetime.now()
                    print("Finalizado","às",datafinal)
                    tempodeestudo   =   datafinal - datainicial
                    print("Estudou",tempodeestudo,"\n")
                    tempoestudseg   = int(tempodeestudo.total_seconds())
                    adicionartempo(materiavalor,tempoestudseg,materiachave,materiageralchave)
                    file = open("contestudando/contadorestudando.py","w")
                    file.write(fr"def contadorestudando():contmateriaestudando = {cont+1}; return contmateriaestudando ")
                    file.close()
                    variaveldependetedocontador = True
                    inputcontinuar = input(">> estudar proxima materia do ciclo?")
                    if inputcontinuar.lower() in"  simyes":
                        pass
                    else: 
                        return False

                    break
        zerarcontarestudando(cont,tarefas,variaveldependetedocontador)        
        cont+=1
    #antes de zerar tem que ver se cont é igual ao maximo
def adicionarmateriajson():
    #trocar por var de aruquivo default
    boolfile = os.path.isfile(('tarefas/dictarefas.py'))
    # criar verificação de tamanho para criar outro arquivo caso passe do tamanho delimitado 500 mb
    if boolfile:
        file = open("tarefas/dictarefas.py","a")
        stgfile = file.read()

        
def adicionartempomateriajson():
    #trocar por var de aruquivo default
    boolfile = os.path.isfile(('tarefas/dictarefas.py'))
    if boolfile:
        pass