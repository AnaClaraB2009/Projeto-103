import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:\\Users\\anacl\\Downloads\\Origem"
to_dir = "C:\\Users\\anacl\\Downloads\\Destino"

class FileEventHandler (FileSystemEventHandler) :
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado")

    def on_deleted(self, event):
        print(f"Opa, alguem excluiu {event.src_path}")

list_of_files = os.listdir(from_dir)

print (list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    print(extension)

    if extension == '': 
        continue
    
    if extension in ['‘.txt’, ‘.doc’, ‘.docx’, ‘.pdf’']:
        path_1 = from_dir + "/" + file_name
        path_2 = to_dir + '/' + "Arquivos_Texto"
        path_3 = to_dir + '/' + "Arquivos_Texto" + '/'  + file_name
    
        if os.path.exists(path_2):
            print ("Movendo" + file_name + ".....")
            shutil.move(path_1,path_3)

        else :
            os.makedirs(path_2)
            print ("Movendo" + file_name + ".....")
            shutil.move(path_1,path_3)

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try: 
    while True: 
        time.sleep(2)
        print("executando ...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()
