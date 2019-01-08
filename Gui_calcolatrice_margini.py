"""""""""
Qui screivero le note per possibili futuri progetti su cui lavorare per poter fare un po di pratica:

Grafica per il programma di margini che ho 




"""""""""

from Calcolatrice_margini import calcolatrice_di_margini                        #importo la mia calcolatrrice di margini
from tkinter import *                                                           #importo la libreria GUI gia presente in python


root = Tk()                                                                     #inserisco una finestra vuota che ho chiamato root
root.geometry("800x600")                                                        #do una dimensione alla mia finestra chiamate root
root.wm_title("Calcolatrice di margini")                                        #modifico il titolo della finestra
root.iconbitmap("Calculator-Android-R.ico")                                     #modifico l'icona della finestra




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