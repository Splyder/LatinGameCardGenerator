from PIL import Image, ImageFont, ImageDraw
import textwrap
from file_gestionnaire import write_file_name

def ouverte_write(question,reponse,model,save_file_name):
  font_title = ImageFont.truetype("data/font_data/arial.ttf",90)
  img = Image.open(model)
  draw = ImageDraw.Draw(img)
  
  lignes = textwrap.wrap(question,13)
  i=0
  for element in lignes:
    draw.text((170,185+(i*90)), lignes[i], (0,0,0), font=font_title)
    i+=1

  lignesr = textwrap.wrap(reponse,13)
  i=0
  for element in lignesr:
    #penser a trouver les co pour ecrire la reponse
    draw.text((150,1220+(-i*90)), lignesr[-i], (57,255,20), font=font_title)
    i+=1
    
  draw = ImageDraw.Draw(img)
  img.save(save_file_name)
  write_file_name(save_file_name,"question_liste.txt")



def ouverte(question_file,model,color,dossier):
  liste=[]
  with open(question_file,"r") as f:
    element=f.read()
    liste=element.split("\n")
    liste1=liste[0::2] 
    liste2=liste[1::2]

  liste_retour2=[]
  for i in range(len(liste1)):
    save_file_name=dossier+"ouverte_"+color+"_"+str(i)+".png"
    ouverte_write(liste1[i],liste2[i],model,save_file_name)
    liste_retour2.append(save_file_name)
  return liste_retour2
#parce qu'elle a le seum

