import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image
class cimage:
    def __init__(self,imgname):
        self.points=[]
        self.i=0
        self.box=()
        self.imname=imgname
        self.window=tk.Tk()
        self.window.title("crop it")
        self.window.configure(background='gray')
        self.img=ImageTk.PhotoImage(Image.open(self.imname))
        self.lbl=tk.Label(self.window,image=self.img)
        self.lbl.pack(fill="both",expand=1)
        print("click the top left and bottom right points for cropping")
        self.lbl.bind('<Button-1>',self.mousepos)
        
    def mousepos(self,event):
          if len(self.points)==4:
              self.box=tuple(self.points)
              self.ccrop()
              return
          self.points.append(event.x)
          self.points.append(event.y)    
          self.i=self.i+1
          print(self.points)
          if len(self.points)==4:
              print("click anywhere to continue")
              
              
    def ccrop(self):
          crop_img=Image.open(self.imname)          
          crop_img=crop_img.crop(self.box)
          savename="cropped_"+self.imname+".jpeg"    
          crop_img.save(savename)
          crop_img=ImageTk.PhotoImage(crop_img)
          self.lbl.configure(image=crop_img)
          self.lbl.image=crop_img          
c=cimage("toph.jpeg")
c.window.mainloop()
          
         
            
             
             
         
         
        
        
        
