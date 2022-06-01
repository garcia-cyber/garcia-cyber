from tkinter import*
from tkinter import ttk

# from ttk import *
import tkinter.messagebox as msg
from tkinter.ttk import Treeview
import mysql.connector as data

def send():
    a = ed2.get()
    b =ed3.get()
    c = S.get()
    d =C.get()
    e = P.get()
    
    
    #connection ou envoie de donnee
    
    sql = data.connect(host='localhost',user = 'root',password = '',database='back_end')
    
    #verification si les champs sont remplit 
    
    if a == '' or b == '' or c == '' or d == '' or c == '':
        msg.showwarning("pas de champs de vides")
    elif c != 'M' and c != 'F' and c != 'f' and c != 'm':
        msg.showerror('seulement '.upper())
      
    else:
        
        send_data = sql.cursor()
        send_data.execute("INSERT INTO clients(noms,telephones,sexes,categorie,province)values('"+ a +"','"+ b +"','"+ c +"','"+ d +"', '"+ e +"')")
        sql.commit()
        send_data.close()
        sql.close() 
        
        
        ed2.delete(0,'end')
        ed3.delete(0,'end')
        S.delete(0,'end')
        C.delete(0,'end')
        P.delete(0,'end')
        msg.showinfo('',"envoie reussi")
         
    
#affiche dans le tableaux

aff = data.connect(host='localhost',user = 'root',password = '',database='back_end')
aff_all = aff.cursor()
req = "SELECT * FROM clients"
aff_all.execute(req) 




requip = aff_all.fetchall()
t = aff_all.rowcount

print(t)

root=Tk()
root.title('gestion des clients'.capitalize())
root.geometry('1200x650')
root.config(bg='teal')
root.resizable(0,0)

boite=Frame(root, width=700, height=250)

sexe=['F','M']
categorie=['detaillant','grosiste']
province=['Kinshasa','Congo_Central','Lubumbashi','Kananga','Kwango','Kwilu','Mbandaka']

# N=Label(boite, text='numero'.capitalize())
# ed1=Entry(boite, bg='grey')
# ed1.place(x=170, y=10)
# N.place(x=10, y=10)

NP=Label(boite, text='nom et postnom'.capitalize())
ed2=Entry(boite, bg='white')
ed2.place(x=170, y=40 ,width=400)
NP.place(x=10, y=40)

T=Label(boite, text='telphone'.capitalize())
ed3=Entry(boite, bg='white')
ed3.place(x=170, y=70,width=400)
T.place(x=10, y=70)

Se=Label(boite, text='sexe'.capitalize())
S=ttk.Combobox(boite, values=sexe, width=5)
S.place(x=170,y=100,width=400)
Se.place(x=10, y=100)

Ca=Label(boite, text='categorie'.capitalize())
C=ttk.Combobox(boite, values=categorie, width=20)
C.place(x=170, y=130,width=400)
Ca.place(x=10, y=130)

Pr=Label(boite, text='province'.capitalize())
P=ttk.Combobox(boite, values=province, width=20)
P.place(x=170, y=160,width=400)
Pr.place(x=10, y=160)

boite.place(x=0,y=20)

btn1=Button(root, text='Enregistre'.capitalize(), border=3, command=send)
btn1.place(x=10, y=310)
btn2=Button(root, text='modifier'.capitalize(), border=3)
btn2.place(x=150, y=310)
btn3=Button(root, text='supprimer'.capitalize(), border=3)
btn3.place(x=270, y=310)
btn4=Button(root, text='quitter'.capitalize(), border=3, command=quit)
btn4.place(x=410, y=310)


#b
boite2=LabelFrame(root, text='affichage',width=1200, height=300)
boite2.place(x = 0 , y = 350)


#btn affiche 

btn_aff = Button(root,text='afficher'.capitalize())
btn_aff.place

af =Treeview(boite2,columns=(1,2,3,4,5,6),show = 'headings')
af.place(x=0 , y = 10)

af.heading(1,text='numero')
af.heading(2 , text='nom et postnom',anchor =W)
af.heading(3 , text='telephones',anchor =W)
af.heading(4 , text='sexes',anchor =W)
af.heading(5 , text='categorie',anchor =W)
af.heading(6 , text='provinces',anchor =W)

for i in requip:
    af.insert('','end' , values=i)
root.mainloop()
