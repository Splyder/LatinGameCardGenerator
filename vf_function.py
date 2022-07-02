from PIL import Image, ImageFont, ImageDraw
import textwrap
from file_gestionnaire import write_file_name

def vf_write(question,reponse,model,save_file_name):
  font_title = ImageFont.truetype("data/font_data/arial.ttf",90)
  img = Image.open(model)
  draw = ImageDraw.Draw(img)
  
  lignes = textwrap.wrap(question,13)
  i=0
  for element in lignes:
    draw.text((170,185+(i*90)), lignes[i], (0,0,0), font=font_title)
    i+=1

  lignes = textwrap.wrap(reponse,13)
  i=0
  for element in lignes:
    draw.text((150,1220+(i*90)), lignes[i], (57,255,20), font=font_title)
    i+=1
    
  draw = ImageDraw.Draw(img)
  img.save(save_file_name)
  write_file_name(save_file_name,"question_liste.txt")

#qcm_write("Question","Reponse 1","Reponse 2","Reponse 3")

def vf(question_file,model,color,dossier):
  liste=[]
  with open(question_file,"r") as f:
    element=f.read()
    liste=element.split("\n")
  listeq=liste[0::2] 
  lister=liste[1::2] 

  liste_retour4=[]
  for i in range(len(lister)):
    save_file_name=dossier+"vf_"+color+"_"+str(i)+".png"
    vf_write(listeq[i],lister[i],model,save_file_name)
    liste_retour4.append(save_file_name)
  return liste_retour4
