""""
Calcolatrice di margini con gui fatta con tkinter:
    1) Calcolatrice dove da una parte ti dice dato un numero x di costo a quanto andrebbe rivenduta la merce come importo netto dato un margine fisso di guadagno
    2) Calcolatrice che ti dice il margine con il quale hai venduto la tua merce con 3 variabili:
        1- Se hai speso piu di quanto hai incassato ti dice che hai pagato piu di quanto hai speso
        2- Se hai speso quanto hai incassato ti dice che hai pagato quanto hai speso
        3- Se hai speso meno di quanto hai incassato ti dice il margine percentuale di guadagno sulla vendita
    Obbiettivi:
        Avere finestre dove inserire testo e pulsanti da premere che eseguano funzioni cosi da mostrare in una nuova finestra il risultato desiderato
    Extra:
        Farlo diventare non troppo brutto esteticamente
"""

from tkinter import *                                                                                                           #importo la libreria GUI gia presente in python e importo tutto *
from tkinter import ttk                                                                                                         #da tkinter importo ttk che posso aggiungere per rendere piu carina la grafica


def Calcolo_prezzo_vendita():                                                                                                   #funzione 1) Calcolatrice
    root_2 = Tk()                                                                                                               #setto che apra una nuova scheda con i suoi parametri
    root_2.geometry("300x40")
    root_2.wm_title("Calcolatrice di margini")
    root_2.iconbitmap("Calculator-Android-R.ico")
    costo_per_vendita = int(num_1.get())                                                                                        #assegno ad una variabile il valore che ricavo da una entry nella gui e impongo che sia un numero
    costo_per_vendita_finito = round((costo_per_vendita * 1.66666666667), 2)                                                    #assegno ad una variabile i calcoli da eseguire
    risultato_vendita = Label (root_2, text="Va venduto ad un prezzo netto di euro " + str(costo_per_vendita_finito))           #mostro i risultati nella nuova finestra
    risultato_vendita.pack()                                                                                                    #assegno i risultati nella scheda a caso tanto verra top centrato perche e' l'unico dato della finestra
    return                                                                                                                      #prima o poi capiro a che cazzo serve return

def Calcolo_margine_vendita():                                                                                                  #funzione 2) Calcolatrice
    root_3 = Tk()                                                                                                               #setto che apra una nuova scheda con i suoi parametri
    root_3.geometry("300x40")
    root_3.wm_title("Calcolatrice di margini")
    root_3.iconbitmap("Calculator-Android-R.ico")
    margine_di_vendita_1 = int(num_2.get())                                                                                     #assegno ad una variabile il valore che ricavo da una entry nella gui e impongo che sia un numero
    margine_di_vendita_2 = int(num_3.get())                                                                                     #assegno ad una variabile il valore che ricavo da una entry nella gui e impongo che sia un numero
    risultato_margine = round((((margine_di_vendita_2 - margine_di_vendita_1) / margine_di_vendita_2)* 100), 2)                 #assegno ad una variabile i calcoli da eseguire
    if margine_di_vendita_1 > margine_di_vendita_2:                                                                             #variabile 1 calcolatrice 2
        no_margine = True
        no_margine = Label (root_3, text="Nessun margine, hai pagato piu di quanto hai speso!")
        no_margine.pack()
    elif margine_di_vendita_1 == margine_di_vendita_2:                                                                          #variabile 2 calcolatrice 2
        in_pari = True
        in_pari = Label (root_3, text="Nessun margine, sei andato in pari!")
        in_pari.pack()
    elif margine_di_vendita_1 < margine_di_vendita_2:                                                                           #variabile 3 calcolatrice 2
        guadagno = True
        guadagno = Label(root_3, text="Il margine e' di " + str(risultato_margine))
        guadagno.pack()
    return                                                                                                                      #prima o poi capiro a che cazzo serve return



root = Tk()                                                                                                                     #inserisco una finestra vuota che ho chiamato root
root.geometry("390x180")                                                                                                        #do una dimensione alla mia finestra chiamate root
root.wm_title("Calcolatrice di margini")                                                                                        #modifico il titolo della finestra
root.iconbitmap("Calculator-Android-R.ico")                                                                                     #modifico l'icona della finestra


header = Label(root, text="Benvenuto nella calcolatrice!", font='Helvetica 10 bold', fg="#111111")                              #metto un header top
header.grid(row=0, column=0)


label_1 = Label(root, text="Inserisci costo del prodotto")                                                                      #faccio dove vanno inseriti i dati della Calcolatrice 1
label_1.grid(row=2, column=0)
num_1 = IntVar()
entry_1 = ttk.Entry(root, textvariable=num_1)
entry_1.grid(row=3, column=0)
button_1 = ttk.Button(root, text="Usa la calcolatrice", command=Calcolo_prezzo_vendita)
button_1.grid(row=5, column=0)


label_2 = Label(root, text="Inserisci costo del prodotto")                                                                      #faccio dove vanno inseriti i dati della Calcolatrice 2
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


root.mainloop()                                                                                                                 #tengo aperta la mia finestra principale in loop senno si chiuderebbe subito





#cose che ho usato per comprendere meglio tkinter prima di fare le cose qui sopra
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

"""
#funzione funzionante senza gli if

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

"""
# divido in 2 parti uguali la finestra

leftFrame = Frame(root)  # , bg="red")
leftFrame.grid(row=2, column=0)
tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)
rightFrame = Frame(root)  # , bg="yellow")
rightFrame.grid(row=2, column=2)
"""