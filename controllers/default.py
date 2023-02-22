from datetime import datetime, timedelta
import time
import shutil
import importlib
import controllers.tarefas.dictarefas as dictarefas

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    linhaslist=file.read().split(";")  
    file.close()
    return linhaslist

def adicionartempo(materia,temposomado,materiachave,materiageral):
    #time em segundos
    #print(materia,temposomado,materiachave,materiageral)
    #print(materia)
    filedictarefas = open("controllers/tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('controllers/tarefas/dictarefas.py','controllers/tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("controllers/tarefas/dictarefas.py","w");filedictarefasapagar.close()

    encontroutipo = False
    encontroumateria = False
    filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
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
            filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
    filedictarefas.close()

def adicionarpositionmateria(materia):
    importlib.reload(dictarefas)
    if str(materia["position"]) == '1':
        #print(materia,temposomado,materiachave,materiageral)
        #print(materia)
        filedictarefas = open("controllers/tarefas/dictarefas.py","r",encoding="UTF-8")
        fileread = filedictarefas.readlines()
        shutil.copyfile('controllers/tarefas/dictarefas.py','controllers/tarefas/dictarefasbackup.py' )
        filedictarefas.close()
        filedictarefasapagar = open("controllers/tarefas/dictarefas.py","w");filedictarefasapagar.close()

        encontroutipo = False
        encontroumateria = False
        filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")

        positionzerado = True
        setaroproximo   =  False
        for linha in fileread:
            #input(linha)
            #input(materia)
            if materia["tipo"] in linha:
                encontroutipo = True
                #print(linha[22:].replace(",",'').lstrip())
            if str(materia["materia"]) in linha[22:]:
                encontroumateria = True
            if  "position" in linha and positionzerado and encontroutipo and encontroumateria:
                linha = (16*" "+fr'"position":0'+(((-len("position:0")+31)))*' '+','+"\n")
                #input(linha)
                filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
                filedictarefas.write(linha)
                encontroumateria = False
                encontroutipo   = False
                positionzerado  = False
                setaroproximo   =   True
                #input("zerando")
            elif setaroproximo and "position" in linha:
                positionzerado  = False
                setaroproximo   = False
                linha = (16*" "+fr'"position":1'+(((-len(f"position:0")+31)))*' '+','+"\n")
                filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
                filedictarefas.write(linha)
                #input("setando")
            else:

                filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
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
            if materiavalor["position"]== 1:
                positionsete = True
        if not positionsete:
            listmateriasAserSetado.append('"'+materiavalor["tipo"]+'"')
    return listmateriasAserSetado

def setarmateriazerada(listmateriasAserSetado):
    filedictarefas = open("controllers/tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('controllers/tarefas/dictarefas.py','controllers/tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("controllers/tarefas/dictarefas.py","w");filedictarefasapagar.close()

   
    filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
    tipo = False;proximopositionseatr = False  
    for linha in fileread:
        #linha[20:-1] para pegar o tipo!
        #print(linha[23:-1])
        if "position" in linha and proximopositionseatr:
            linha = (16*" "+fr'"position":1'+(((-len(f'"position:1"')+31)))*' '+','+"\n")
            filedictarefas.write(linha)
            proximopositionseatr = False
        # terminar aquiusaaaaaaaa
        tipovalor=(linha[23:-2].strip())
        if "tipo" in linha:
            tipo = True
        if  tipovalor in listmateriasAserSetado and tipo:
            #resolver escrver na hora certa 
            input(str(tipo)+" if certo")
            proximopositionseatr = True
            cont=0
            for tipodalista in listmateriasAserSetado:
                if tipo == tipodalista:
                    del listmateriasAserSetado[cont]
                    input(linha)
                cont+=1
            del listmateriasAserSetado[0]
        
        else:
            #print("escrevbendo padrao")
            filedictarefas.write(linha)
    filedictarefas.close()

def restartnodictarefas():
    shutil.copyfile('controllers/tarefas/dictarefasdefault.py','controllers/tarefas/dictarefas.py' )