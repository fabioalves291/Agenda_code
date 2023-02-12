from tarefas import *

def lerarquivo(endereço):
    linhaslist= list()
    file = open(endereço,'r',encoding="UTF-8")
    for linhas in file:
        fileread = file.readline()
        linhaslist.append(fileread)
        print(fileread)
    
    file.close()
    return fileread

    
def adicionartempo(materia,tempodeestudo):
    #print(tarefas)
    lista = lerarquivo("controllers/tarefas/tarefas.py")
    lista = str(lista)
    lista = lista.split(";")
    
    print(materia)
    print(tempodeestudo)

def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))