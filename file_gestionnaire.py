import os

def write_file_name(file_name,save_data_file):
  with open(save_data_file,"a")as sdf:
    sdf.write("\n"+file_name)

def delete_last_save_file():
  os.remove() 

def read_save_file():
  with open("question_liste.txt","r") as f:
    file=f.read()
  liste=file.split("\n")
  for i in range(len(liste)):
    liste[i]=liste[i].replace("\n","v")
  return file
