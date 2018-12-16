import tkinter as tk
import random
import winsound
from tkinter import *
from PIL import ImageTk,Image
class game:
    def __init__(self,imgname):
        self.imgfile=imgname
        self.window=tk.Tk()
        self.window.title("image game")
        self.window.configure(background='gray')
        self.lbl=tk.Label(self.window,text="click on the start to continue")
        self.lbl.grid(row=1,column=0,sticky=N+S+E+W)
        self.img2=Image.open(r"C:\Users\HP\Desktop\quest.jpeg")
        self.img2=self.img2.resize((255,255))
        self.img=Image.open(self.imgfile)
        self.img=self.img.resize((255,255))
        self.img1=ImageTk.PhotoImage(self.img)
        self.orilist=[]
        self.templist=[]
        self.imglbl=tk.Label(self.window,image=self.img1)
        self.imglbl.image=self.img1
        self.imglbl.grid(row=2,column=0,sticky=N+S+E+W)
        self.startbt=tk.Button(self.window,text="start",command= self.start).grid(row=3,column=0,sticky=N+S+E+W)
        self.resultbt=tk.Button(self.window,text="check result",command=self.resultcheck,bg="blue")
        self.resultlbl=tk.Label(self.window)
        x=[0,0]
        y=[85,85]
        for i in range(3):
            for j in range(3):
                box=(x[0],x[1],y[0],y[1])
                print(box)
                self.orilist.append(ImageTk.PhotoImage(self.img.crop(box)))
                x[0]=x[0]+85
                y[0]=y[0]+85
            x[0]=0
            x[1]=y[1]
            y[0]=x[0]+85
            y[1]=x[1]+85
            self.lbllist=[]
        for i in range(9):
            self.lbllist.append(tk.Label(self.window,image=self.orilist[i]))
            self.lbllist[i].image=self.orilist[i]
        print(type(self.lbllist))    
        self.shufflelist=self.lbllist.copy()
        random.shuffle(self.shufflelist)
        print(type(self.shufflelist))
                

    def start(self):
        winsound.PlaySound('naruto.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
        r=3
        c=1        
        for i in range(9):
            self.shufflelist[i].bind('<Button-1>',self.swap)
            self.shufflelist[i].grid(row=r,column=c,sticky=N+S+E+W)
            c=c+1
            if i==2 or i==5:
                r=r+1
                c=1
        self.resultbt.grid(row=4,column=0,sticky=N+S+E+W,rowspan=5)       
        ques=ImageTk.PhotoImage(self.img2)        
        self.imglbl.configure(image=ques)
        self.imglbl.image=ques

    def swap(self,event):
        if len(self.templist)==1:
            self.templist.append(event.widget)
            temp=self.templist[0].image
            self.templist[0].image=self.templist[1].image
            self.templist[1].image=temp            
            self.templist[0].configure(image=self.templist[0].image)
            self.templist[1].configure(image=self.templist[1].image)
            self.templist=[]
            return
        self.templist.append(event.widget)

    def resultcheck(self):
        ccount=0
        for i in range(len(self.orilist)):
            if(self.orilist[i]==self.shufflelist[i].image):
                ccount=ccount+1
        if ccount==len(self.shufflelist):
            ccount=0
            self.resultlbl.grid(row=1,column=1,sticky=N+S+E+W,rowspan=2,columnspan=4)
            self.resultlbl.config(text="success",bg="green")
            self.resultlbl.bg="green"
            self.resultlbl.text="success"
            winsound.PlaySound(None,winsound.SND_PURGE)
        else:
            self.resultlbl.grid(row=1,column=1,sticky=N+S+E+W,rowspan=2,columnspan=4)
            self.resultlbl.config(text="incorrect",bg="red")
            self.resultlbl.text="incorrect"
            self.resultlbl.bg="red"
            
                     
            
            
g=game("toph.jpeg")
g.window.mainloop()

                
        
        
        
        
