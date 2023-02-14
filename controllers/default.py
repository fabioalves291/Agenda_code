from tarefas import *
from controllers.tarefas.dictarefas import *
from datetime import datetime, timedelta
import time
import shutil

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    linhaslist=file.read().split(";")  
    file.close()
    return linhaslist

    
def adicionartempo(materia,tempodeestudo):
    #time em segundos
    print(tempodeestudosomado)

    time = materia["time"]
    filedictarefas = open("controllers/tarefas/dictarefas.py","r",encoding="UTF-8")
    fileread = filedictarefas.readlines()
    shutil.copyfile('controllers/tarefas/dictarefas.py','controllers/tarefas/dictarefasbackup.py' )
    filedictarefas.close()
    
    filedictarefas = open("controllers/tarefas/dictarefas.py","w");filedictarefas.close()
    encontroutipo = False
    encontroumateria = False
    for linha in fileread:
        #print(linha)
        if materia["tipo"] in linha:
            encontroutipo = True
            #print(linha[22:].replace(",",'').lstrip())
        if str(materia["materia"]) in linha[22:]:
            encontroumateria = True
        if  "time" in linha and encontroutipo       and encontroumateria:
            tempodeestudosomado = tempodeestudo + int(materia["time"]
            ## criar funcao  pegar o numero para poder somar.
            linha = (12*" "+fr'"time":{tempodeestudo}'+(((-len(f"time:{tempodeestudosomado}")+30)))*' '+','+"\n")
            #input(":time")
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