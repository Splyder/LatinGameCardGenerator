from fpdf import FPDF
from PIL import Image

def makePdf_4img(pdfFileName, listPages):
    width, height = 1080,1440

    pdf = FPDF(unit = "pt", format = [width, height])
    i=0
    z=len(listPages)//4
    for i in range(z):
      pdf.add_page()
      pdf.image(x = 0, y = 0, w = 504, h =720, name = listPages[i*4],type="png")
      pdf.image(x = 0, y = 720, w = 504, h =720, name = listPages[i*4+1],type="png")
      pdf.image(x = 504, y = 0, w = 504, h =720, name = listPages[i*4+2],type="png")
      pdf.image(x = 504, y = 720, w = 504, h =720, name = listPages[i*4+3],type="png")
        
    pdf.output(pdfFileName, "F")

#makePdf("test5",["j1.png","j2.png"],"test_dir")