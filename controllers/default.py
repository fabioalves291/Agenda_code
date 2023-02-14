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

    time = materia["time"]
    print((int(time))+tempodeestudo,"segundos")
    filedictarefas = open("controllers/tarefas/dictarefas.py","r")
    fileread = filedictarefas.readlines()
    for linhas in fileread:
        print(linhas)
        input()


def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))