from datetime import datetime, timedelta
import time
import shutil
import importlib
import tarefas.dictarefas as dictarefas

def adicionartempo(materia,temposomado,materiachave,materiageral):
    #time em segundos
    #print(materia,temposomado,materiachave,materiageral)
    #print(materia)
    filedictarefas = open("tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('tarefas/dictarefas.py','tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("tarefas/dictarefas.py","w");filedictarefasapagar.close()

    encontroutipo = False
    encontroumateria = False
    filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
    for linha in fileread:
        #print(linha)
        if materia["tipo"] in linha:
            encontroutipo = True
            #print(linha[22:].replace(",",'').lstrip())
        if str(materia["materia"]) in linha[22:]:
            encontroumateria = True
        if  "time" in linha and encontroutipo and encontroumateria:
            linha = (16*" "+fr'"time":{temposomado+materia["time"]}'+(((-len(f"time:{temposomado}")+30)))*' '+','+"\n")
            #input(linha)
            encontroumateria = False
            encontroutipo = False
            filedictarefas.write(linha)
        else:
            filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
    filedictarefas.close()

def adicionarpositionmateria(materia):
    importlib.reload(dictarefas)
    if str(materia["position"]) == '1':
        #print(materia,temposomado,materiachave,materiageral)
        #print(materia)
        inputcontinuar= input(">> iniciar estudo da materia tipo "+materia["tipo"]+" topico "+materia["materia"]+':')
        if inputcontinuar.lower() in"  simyes":
            pass
        else: 
            return False
        filedictarefas = open("tarefas/dictarefas.py","r",encoding="UTF-8")
        fileread = filedictarefas.readlines()
        shutil.copyfile('tarefas/dictarefas.py','tarefas/dictarefasbackup.py' )
        filedictarefas.close()
        filedictarefasapagar = open("tarefas/dictarefas.py","w");filedictarefasapagar.close()

        encontroutipo = False
        encontroumateria = False
        filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")

        positionzerado = True
        setaroproximo   =  False
        for linha in fileread:
            print(linha)
            #input(materia)
            if materia["tipo"] in linha:
                encontroutipo = True
                
            if str(materia["materia"]) in linha[22:]:
                encontroumateria = True
            if  "position" in linha and positionzerado and encontroutipo and encontroumateria:
                linha = (16*" "+fr'"position":0'+(((-len("position:0")+31)))*' '+','+"\n")
                
                filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
                filedictarefas.write(linha)
                encontroumateria = False
                encontroutipo   = False
                positionzerado  = False
                setaroproximo   =   True
                input("zerando")
            elif setaroproximo and "position" in linha:
                positionzerado  = False
                setaroproximo   = False
                linha = (16*" "+fr'"position":1'+(((-len(f"position:0")+31)))*' '+','+"\n")
                filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
                filedictarefas.write(linha)
                input("setando")
            else:

                filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
                filedictarefas.write(linha)
                #input("continuando")
        filedictarefas.close()

        return  True
    else:
        #print("false")
        return False

def verificarmaterinotset():
    importlib.reload(dictarefas)
    listmateriasAserSetado = list()
    tarefas = dictarefas.defdictarefas()
    for materiageralchave, materiageralvalor in tarefas.items():
        positionsete = False
        for materiachave, materiavalor in tarefas[materiageralchave].items():
            
            if materiavalor["position"]==1:
                positionsete = True
        if not positionsete:
            listmateriasAserSetado.append('"'+materiavalor["tipo"]+'"')
    return listmateriasAserSetado

def setarmateriazerada(listmateriasAserSetado):
    filedictarefas = open("tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('tarefas/dictarefas.py','tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("tarefas/dictarefas.py","w");filedictarefasapagar.close()

    tipo = False;proximopositionseatr = False  
    for linha in fileread:
        #linha[20:-1] para pegar o tipo!
        #print(linha[23:-1])
        if "position" in linha and proximopositionseatr:
            linha = (16*" "+fr'"position":1'+(((-len(f'"position:1"')+31)))*' '+','+"\n")
            filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
            filedictarefas.close()
            proximopositionseatr = False
        else:
            #print("escrevendo padrao")
            filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
            filedictarefas.close()
        tipovalor=(linha[23:-2].strip())
        
        if "tipo" in linha:
            tipo = True
        if  tipovalor in listmateriasAserSetado and tipo:      
            proximopositionseatr = True
            cont=0
            for tipodalista in listmateriasAserSetado:
                if tipovalor == tipodalista:
                    del listmateriasAserSetado[cont]
                cont+=1

def zerarcontarestudando(cont,tarefas, variaveldependete):
    if cont >= len(tarefas) and variaveldependete :
        file = open("contestudando/contadorestudando.py","w")
        file.write(fr"def contadorestudando():contmateriaestudando = {1}; return contmateriaestudando ")
        file.close()
def restartnodictarefas():
    shutil.copyfile('tarefas/dictarefasdefault.py','tarefas/dictarefas.py' )