from tarefas import *
from controllers.tarefas.dictarefas import *
from datetime import datetime, timedelta
import time

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    linhaslist=file.read().split(";")  
    file.close()
    return linhaslist

    
def adicionartempo(materia,tempodeestudo):
    #print(tarefas)
    #time em segundos
    lista = lerarquivo("controllers/tarefas/tarefas.py")
    time = materia["time"]
    time=1
    print((int(time))+tempodeestudo,"segundos")


def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))