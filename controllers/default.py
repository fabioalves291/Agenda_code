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
    print(materia,temposomado,materiachave,materiageral)
    #print(materia)
    filedictarefas = open("controllers/tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('controllers/tarefas/dictarefas.py','controllers/tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("controllers/tarefas/dictarefas.py","w");filedictarefasapagar.close()
    input("apagado")
    
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
            #print(linha[18:-1])
            ## criar funcao  pegar o numero para poder somar.
            linha = (12*" "+fr'"time":{temposomado+materia["time"]}'+(((-len(f"time:{temposomado}")+30)))*' '+','+"\n")
            print(linha)
            input(":time")
            encontroumateria = False
            encontroutipo = False
            filedictarefas.write(linha)
        else:
            filedictarefas = open("controllers/tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
    filedictarefas.close()

def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))
