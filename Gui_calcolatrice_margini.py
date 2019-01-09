"""""""""
Qui screivero le note per possibili futuri progetti su cui lavorare per poter fare un po di pratica:

Grafica per il programma di margini che ho 




"""""""""

from tkinter import *                                                           #importo la libreria GUI gia presente in python
from tkinter import ttk
#import tkinter.ttk


def Calcolo_prezzo_vendita():
    root_2 = Tk()
    root_2.geometry("300x40")
    root_2.wm_title("Calcolatrice di margini")
    root_2.iconbitmap("Calculator-Android-R.ico")
    costo_per_vendita = int(num_1.get())
    costo_per_vendita_finito = round((costo_per_vendita * 1.66666666667), 2)
    risultato_vendita = Label (root_2, text="Va venduto ad un prezzo netto di euro " + str(costo_per_vendita_finito))
    risultato_vendita.pack()
    return

def Calcolo_margine_vendita():
    root_3 = Tk()
    root_3.geometry("300x40")
    root_3.wm_title("Calcolatrice di margini")
    root_3.iconbitmap("Calculator-Android-R.ico")
    margine_di_vendita_1 = int(num_2.get())
    margine_di_vendita_2 = int(num_3.get())
    risultato_margine = round((((margine_di_vendita_2 - margine_di_vendita_1) / margine_di_vendita_2)* 100), 2)
    guadagno = Label (root_3, text="Il margine e' di " + str(risultato_margine))
    guadagno.pack()
    return
"""    
    if margine_di_vendita_1 > margine_di_vendita_2:
        no_margine = Label (root, text="Nessun margine, hai pagato piu di quanto hai speso!")
        no_margine.grid(row=6, column=1)
    elif margine_di_vendita_1 == margine_di_vendita_2:
        in_pari = Label (root, text="Nessun margine, sei andato in pari!")
        in_pari.grid(row=6, column=1)
    elif margine_di_vendita_1 < margine_di_vendita_2:
        guadagno = Label(root, text="Va venduto ad un prezzo netto di euro " + str(risultato_margine))
        guadagno.grid(row=6, column=1)
"""


root = Tk()  # inserisco una finestra vuota che ho chiamato root
root.geometry("390x180")  # do una dimensione alla mia finestra chiamate root
root.wm_title("Calcolatrice di margini")  # modifico il titolo della finestra
root.iconbitmap("Calculator-Android-R.ico")  # modifico l'icona della finestra


header = Label(root, text="Benvenuto nella calcolatrice!", font='Helvetica 10 bold', fg="#111111")
header.grid(row=0, column=0)

"""
# divido in 2 parti uguali la finestra
leftFrame = Frame(root)  # , bg="red")
leftFrame.grid(row=2, column=0)
tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)
rightFrame = Frame(root)  # , bg="yellow")
rightFrame.grid(row=2, column=2)
"""

# faccio dove vanno inseriti i dati del primo programma
label_1 = Label(root, text="Inserisci costo del prodotto")
label_1.grid(row=2, column=0)
num_1 = IntVar()
entry_1 = ttk.Entry(root, textvariable=num_1)
entry_1.grid(row=3, column=0)
button_1 = ttk.Button(root, text="Usa la calcolatrice", command=Calcolo_prezzo_vendita)
button_1.grid(row=5, column=0)

# faccio dove vanno inseriti i dati del secondo programma
label_2 = Label(root, text="Inserisci costo del prodotto")
label_2.grid(row=2, column=1)
num_2 = IntVar()
entry_2 = ttk.Entry(root, textvariable=num_2)
entry_2.grid(row=3, column=1)

label_3 = Label(root, text="Inserisci a quanto lo hai venduto")
label_3.grid(row=4, column=1)
num_3 = IntVar()
entry_3 = ttk.Entry(root, textvariable=num_3)
entry_3.grid(row=5, column=1)
button_3 = ttk.Button(root, text="Usa la calcolatrice", command=Calcolo_margine_vendita)
button_3.grid(row=7, column=1)


root.mainloop()                                                                 #per tenere la finestra aperta per evitare che si chiuda subito



"""
topFrame = Frame(root)                                  #creo un frame top in root
topFrame.pack()                                         #lo packo
botFrame = Frame(root)                                  #creo un frame bot
botFrame.pack(side=BOTTOM)                              #lo packo e specifico che va bot

button1 = Button(topFrame, text="premi v....", fg="red")     #creo bottoni e assegno dove vanno, cosa contengono ed il colore
button2 = Button(topFrame, text="premi m....", fg="green")
button3 = Button(botFrame, text="prova", fg="#BDB76B")       #posso anche usaere i codici dei colori

button1.pack(side=LEFT)                                          #li pacco tutti e cio serve per farli vedere, prima li creo poi vanno "fatti vedere"
button2.pack(side=LEFT)                                          #cosi vengono packati uno sopra all'altro e qui posso con parametro decidere dove metterli
button3.pack(side=BOTTOM)
"""

"""
one = Label(root, text="one", bg="red", fg="green")     #posso anche inserire o background o foreground e anche decidere se riempire la pagina per x o y del colore scelto in bg
one.pack()
two = Label(root, text="two", bg="black", fg="white")
two.pack(fill=X)
three = Label(root, text="three", bg="purple", fg="yellow")
three.pack(side=LEFT, fill=Y)
"""

"""
Thelable1 = Label(root, text="name", fg="red")
Thelable2 = Label(root, text="password")
entry1 = Entry(root)                                    #In questa libreria entry e' l'equivalente di input
entry2 = Entry(root)

Thelable1.grid(row=0, column=0, sticky=E)               #grid e' come pack ma ti crea una griglia dove puoi scegliere colonna e riga. Sticky e' un comando per dove allineare cio che ho inserito e si usano i punti cardinali E;N;W;S;
Thelable2.grid(row=1, column=0, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
"""

"""
button_1 = Button(root, text="Usa la calcolatrice", fg="white", bg="black", command=calcolatrice_di_margini)        #con command posso inserire una funzione da eseguire quando viene premuto il pulsante
button_1.pack()
"""

"""
#faccio il footer

import tkinter.messagebox


status = Label(root, text="Preparing to do nothing....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
"""

"""
#aggiungere immagini e icone
#devo aggiungere le immagini nella stessa directory

photo = PhotoImage(file="Logo Bax.png")
label = Label(root, image=photo, heigh=200, width=200)
label.pack()
"""