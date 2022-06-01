from tkinter import *
import mysql.connector as data
from tkinter import ttk
from tkinter.messagebox import *

#---------------------partie fonction

def btn_click():
    user = entr1.get()
    pwd  = entr2.get()

    #print(f" bonjour { user} votre mot de passe {pwd}")

    #verification du mot de passe

    if user == '' or pwd == '':
        showerror("error", "veillez remplire les champs")
    elif user == 'python' or user == '123' or user == 'jophia' and pwd == 'python' or pwd == '123' :
        entr1.delete(0, 'end')
        entr2.delete(0, 'end')
        showinfo(" ", "connexion reussi")

        # to_ask = showinfo("voulez vous ")

        # if to_ask == 'ok':
        #     app.destroy()
        
        #creation de la fenetre d'enregistrement 
        
        sign_up = Toplevel()
        sign_up.geometry("1400x800")
        sign_up.resizable(0,0)
        
        fr =Frame(sign_up,bg= 'steelblue')
        fr.place(x = 1 , y = 2,width=1400,height=300)
        
        tj = ttk.Treeview(fr, columns=(1,2,3,4,5,6,7,8), show='headings')
        tj.place(x = 0, y = 2)
        tj.heading(1,text='numero')
        tj.heading(2,text='noms')
        tj.heading(3,text='prenom')
        tj.heading(4,text='ville')
        tj.heading(5,text='sexe')
        tj.heading(6,text='faculte')
        tj.heading(7,text='promotion')
        tj.heading(8,text='telephone')
        
        sign_up.mainloop()


#---------------------fin de la partie fonction

app = Tk()
app.title('connexion'.upper())
# app.geometry("1400x800")
app.geometry("250x350")
app.resizable(0,0)
# app.config(bg='#111')

com = Frame(app,bg='#111')
com.place(x = 0, y = 0, height=60 ,width=250)

connexion_fr = Label(com,text='login'.upper(),border=5,fg='whitesmoke',bg='#111')
connexion_fr.place(x = 0 , y = 20)


text1 = Label(app,text='username'.capitalize())
text1.place(x = 20 , y = 100)

entr1 = Entry(app)
entr1.place(x = 20, y= 120,width=200,height=29)


text2 = Label(app,text='password'.capitalize())
text2.place(x = 20 , y = 170)

entr2 = Entry(app,show= '*')
entr2.place(x = 20, y= 190,width=200,height=29)


#bouton de connexion

btn_con = Button(app,text='connexion',command=btn_click)
btn_con.place(x =75 , y = 250)





app.mainloop()