from tarefas import *

def lerarquivo(endereço,modo):
    file = open(endereço,modo,encoding="UTF-8")
    linhaslist= list()
    for linhas in file:
        fileread = file.readline()
        linhaslist.append(fileread)
    print((linhaslist))
    file.close()
    return fileread
    
def adicionartempo(materia,tempodeestudo):
    #print(tarefas)
    print(materia)
    print(tempodeestudo)

def adicionarpositionmateria(materia):
    print() 

def adicionarposition(tarefa):
    print(lerarquivo("controllers/tarefas/tarefas.py","r"))
    



