from datetime import datetime, timedelta
import time
import shutil

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
            linha = (12*" "+fr'"time":{temposomado+materia["time"]}'+(((-len(f"time:{temposomado}")+31)))*' '+','+"\n")
            #input(linha)
            encontroumateria = False
            encontroutipo = False
            filedictarefas.write(linha)
        else:
            filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
    filedictarefas.close()

def adicionarpositionmateria(materia):
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
                linha = (12*" "+fr'"position":0'+(((-len(f"position:0")+31)))*' '+','+"\n")
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
                linha = (12*" "+fr'"position":1'+(((-len(f"position:0")+31)))*' '+','+"\n")
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
        print("false")
        return False


def restartnodictarefas():
    shutil.copyfile('controllers/tarefas/dictarefasdefault.py','controllers/tarefas/dictarefas.py' )