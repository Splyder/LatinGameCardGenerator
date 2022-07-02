from os import makedirs
from PIL import Image
from qcm_function import *
from vf_function import *
from ouverte_function import *
from bonus_function import *
from file_gestionnaire import*
from img_to_pdf import makePdf_4img


def generator(x):
  liste=[]
  makedirs(x)
  x=x+"/"
  color_list=["rouge","bleu","jaune","vert"]
  for color in color_list:
    makedirs(x+color)
    makedirs(x+color+"/vf")
    liste+=vf("data/question_data/question_vf_"+color+".txt","data/model/"+color+"_vf.png",color,x+color+"/vf/")
    makedirs(x+color+"/qcm")
    liste+=qcm("data/question_data/question_qcm_"+color+".txt","data/model/"+color+"_qcm.png",color,x+color+"/qcm/")
    makedirs(x+color+"/ouverte")
    liste+=ouverte("data/question_data/question_1_"+color+".txt","data/model/"+color+"_1.png",color,x+color+"/ouverte/")
  makedirs(x+"bonus")
  liste+=bonus(x+"bonus/")
  makedirs(x+"pdf")
  for i in range(len(liste)//4):
    makePdf_4img(x+"pdf"+"/a_imprimer"+str(i)+".pdf",liste[i*4:(i*4)+4])
  
generator("generation")


def resize(file_name,new_file_name,width,height):
  img = Image.open(file_name)
  img = img.resize((width, height), Image.ANTIALIAS)
  img.save(new_file_name)


x="vfgenere" 
liste=[]
makedirs(x)
x=x+"/"
color_list=["rouge","bleu","jaune","vert"]
for color in color_list:
  makedirs(x+color)
  makedirs(x+color+"/vf")
  liste+=vf("data/question_data/question_vf_"+color+".txt","data/model/"+color+"_vf.png",color,x+color+"/vf/")

makePdf_4img("generator/"+"pdf"+"/a_imprimer"+".pdf",liste)