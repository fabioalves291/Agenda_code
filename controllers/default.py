from tarefas import *
import datetime

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    linhaslist=file.read().split(";")  
    file.close()
    return linhaslist

    
def adicionartempo(materia,tempodeestudo):
    #print(tarefas)
    lista = lerarquivo("controllers/tarefas/tarefas.py")
    print((lista[1][28:-1]));input()
    print(materia["materia"])
    print(tempodeestudo+datetime(materia["time"]))

def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))