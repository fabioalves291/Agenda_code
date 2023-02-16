from tarefas.dictarefas import *
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
    filedictarefas = open("tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('tarefas/dictarefas.py','tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    filedictarefasapagar = open("tarefas/dictarefas.py","w");filedictarefasapagar.close()
    encontroutipo = False
    input("apagado")
    encontroumateria = False
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
            #input(":time")
            encontroumateria = False
            encontroutipo = False
            filedictarefas.write(linha)
        else:
            filedictarefas = open("tarefas/dictarefas.py","a",encoding="UTF-8")
            filedictarefas.write(linha)
    filedictarefas.close()



def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))
