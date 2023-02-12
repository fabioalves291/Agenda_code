from tarefas import *

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    linhaslist=file.read().split(";")  
    file.close()
    return linhaslist

    
def adicionartempo(materia,tempodeestudo):
    #print(tarefas)
    lista = lerarquivo("controllers/tarefas/tarefas.py")
    print(lista);input()
    print(materia)
    print(tempodeestudo)

def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))