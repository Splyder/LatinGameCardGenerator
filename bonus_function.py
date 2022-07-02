from PIL import Image, ImageFont, ImageDraw
import textwrap
from file_gestionnaire import write_file_name

def bonus_write(texte,model,save_file_name):
  font_title = ImageFont.truetype("data/font_data/arial.ttf",90)
  img = Image.open(model)
  draw = ImageDraw.Draw(img)
  
  lignes = textwrap.wrap(texte,15)
  i=0
  for element in lignes:
    draw.text((170,350+(i*90)), lignes[i], (0,0,0), font=font_title)
    i+=1
    
  draw = ImageDraw.Draw(img)
  img.save(save_file_name)
  write_file_name(save_file_name,"question_liste.txt")

#qcm_write("Question","Reponse 1","Reponse 2","Reponse 3")

def bonus(dossier):
  liste=[]
  with open("data/question_data/carte_chance.txt","r") as f:
    element=f.read()
    liste=element.split("\n")

  liste2=[]
  with open("data/question_data/carte_malchance.txt","r") as f:
    element=f.read()
    liste2=element.split("\n")
  
  liste_retour=[]
  for i in range(len(liste)):
    save_file_name=dossier+"bonus_"+str(i)+".png"
    bonus_write(liste[i],"data/model/carte_c.png",save_file_name)
    liste_retour.append(save_file_name)

  for i in range(len(liste2)):
    save_file_name=dossier+"bonus_"+str(i+len(liste))+".png"
    bonus_write(liste2[i],"data/model/carte_m.png",save_file_name)
    liste_retour.append(save_file_name)
  
  return liste_retour