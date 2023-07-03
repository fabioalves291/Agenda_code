#! python3.10
from controllers.tarefasfuncao import adicionartempomateria,adicionarmateriaespecifica
from controllers.default import *
import logging
import datetime
import os 

if __name__ == "__main__":
    while True:
        try:
            print(">> iniciando...") 
            time.sleep(2)
            
    
            if input(">> deseja estudar alguma materia especifica?\n>> ").lower() in"  simyes":
                adicionarmateriaespecifica()
                        
            print(verificarmaterinotset(),'ciclos finalizados')
            setarmateriazerada(verificarmaterinotset())
            adicionartempomateria()
            input(">> finalizado:")
        except  Exception as e :
            print(e)
            logging.basicConfig(filename="log/log.log",level=logging.DEBUG,filemode="a")
            logger = logging.getLogger()
            logger.exception("date:"+str(datetime.datetime.now)+"erro:\n"+str(e))

    

        
