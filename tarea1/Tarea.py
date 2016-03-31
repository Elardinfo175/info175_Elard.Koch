from Tkinter import *
from tkMessageBox import *
import Tkinter
from Cesar import *
from cenit import *


listaABC=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listaPolar=["i","b","p","d","o","f","g","h","a","j","k","n","m","l","p","c","q","t","s","r","u","v","w","x","y","z"]



#window options
pw=Tkinter.Tk()
pw.resizable(0,0)
pw.geometry("500x350+400+200")
pw.title("Tarea Encrypt")

Check1=IntVar()
Check2=IntVar()
Co=StringVar()
Cn=StringVar()
Check1.set(0)
Check2.set(0)

#text
Entr=Entry(width="40",textvariable=Co).place(x=110,y=20)
Entr1=Entry(width="2",textvariable=Cn).place(x=110,y=160)

#labels
sme=Label(text="Seleccione metodo de encriptacion").place(x=145,y=90)
salida=Label(width="40",height="3").place(x=110,y=250)
cesarlb=Label(text="Especifique el salto para la encriptacion cesar").place(x=130,y=160)
resultado=Label(text="Resultado: ").place(x=110,y=230)
insertF=Label(text="Ingrese la frase a Encriptar").place(x=170,y=0)

#checkButton
cenitpolar=Checkbutton(pw,text="Cenit-polar",variable=Check1,onvalue=1,offvalue=0).place(x=240,y=110)
cesar=Checkbutton(pw,text="Cesar",variable=Check2,onvalue=1,offvalue=0).place(x=170,y=110)

#button

emc=Button(pw,text="Encriptar",command=lambda:checker(listaABC,listaPolar)).place(x=205,y=190)

def checker(ls1,ls2):
 if(Check1.get()!=Check2.get()):
  if(Check1.get()==1):
   f=str(Co.get())
   f=cambiar(ls1,ls2,f)
   finalLabel=Label(text=f,width="40",height="3").place(x=110,y=250)
  else:
   if(not (str(Cn.get())).isdigit()):
    showinfo(title='Error', message='Ingrese un digito')
   else:
    f=trasladar(str(Co.get()),int(Cn.get()))
    print(trasladar(str(Co.get()),int(Cn.get())))
    finalLabel=Label(text=f,width="40",height="3").place(x=110,y=250)
 else:
  showinfo(title='Error', message='Escoja Cenit-Polar o Cesar')
 


pw.mainloop();
