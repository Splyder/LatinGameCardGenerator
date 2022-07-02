from PIL import Image, ImageFont, ImageDraw
import textwrap
from file_gestionnaire import write_file_name

def qcm_write(question,reponse1,reponse2,reponse3,vrai_reponse,model,save_file_name):
  font_title = ImageFont.truetype("data/font_data/arial.ttf",50)
  font_paragraphe = ImageFont.truetype("data/font_data/arial.ttf",50)
  img = Image.open(model)
  draw = ImageDraw.Draw(img)
  
  lignes = textwrap.wrap(question,19)
  i=0
  for element in lignes:
    draw.text((170,185+(i*50)), lignes[i], (0,0,0), font=font_title)
    i+=1
  
  lignes1 = textwrap.wrap(reponse1,19)
  i=0
  for element in lignes1:
    draw.text((280,700+(i*50)), lignes1[i], (0,0,0), font=font_paragraphe)
    i+=1

  lignes2 = textwrap.wrap(reponse2,19)
  i=0
  for element in lignes2:
    draw.text((280,950+(i*50)), lignes2[i], (0,0,0), font=font_paragraphe)
    i+=1

  lignes3 = textwrap.wrap(reponse3,19)
  i=0
  for element in lignes3:
    draw.text((280,1170+(i*50)), lignes3[i], (0,0,0), font=font_paragraphe)
    i+=1

  lignes4 = textwrap.wrap(vrai_reponse,19)
  i=0
  for element in lignes4:
    draw.text((280,1220+(i*50)), lignes4[i], (57,255,20), font=font_paragraphe)
    i+=1
  

  draw = ImageDraw.Draw(img)
  img.save(save_file_name)
  write_file_name(save_file_name,"question_liste.txt")

#qcm_write("Question","Reponse 1","Reponse 2","Reponse 3")

def qcm(question_file,model,color,dossier=""):
  liste_total=[]
  with open(question_file,"r") as f:
    element=f.read()
  liste_total=element.split("\n")
  liste_question=liste_total[0::5] 
  liste_reponse_a=liste_total[1::5] 
  liste_reponse_b=liste_total[2::5] 
  liste_reponse_c=liste_total[3::5] 
  vrai_reponse=liste_total[4::5] 
  liste_retour3=[]
  for i2 in range(len(vrai_reponse)):
    save_file_name=dossier+"qcm_"+color+"_"+str(i2)+".png"
    qcm_write(liste_question[i2],liste_reponse_a[i2],liste_reponse_b[i2],liste_reponse_c[i2],vrai_reponse[i2],model,save_file_name)
    liste_retour3.append(save_file_name)
  return liste_retour3