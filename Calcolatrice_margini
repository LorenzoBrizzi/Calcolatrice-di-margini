def calcolatrice_di_margini():
    a = 0

    while a == 0:
        print(
                '--------------------------------------------------------------------------------------------------------------')
        int = input("Cosa voui fare? Se vuoi calcolare i margini premi [m] + invio, se vuoi trovare il prezzo di vendita con il 40% di margine partendo dal costo premi [v]+ invio!")

        if int == "m":

            from sys import exit

            def error():
                print("Devi scrivere un numero!")


            def get_number(question):
                # start the loop and only break out of it if the input given is a number
                while True:
                    try:
                        cost = float(input(question))
                    except ValueError:
                        error()
                        continue
                    except Exception as err:
                        print(err)
                        exit()

                    # just to make sure!
                    if isinstance(cost, float):
                        break
                    else:
                        error()
                return cost


            def calc(cost, sale):
                if cost > sale:
                    print("Nessun margine, hai pagato piu di quanto hai speso! ")
                elif cost == sale:
                    print("Sei andato in pari! ")
                elif cost < sale:
                    print("Il margine di guadagno e' del ", ((sale - cost) / sale) * 100, "%")


            if True:
                # call the get_number function as pass the question to it
                print(
                    '--------------------------------------------------------------------------------------------------------------')
                cost = get_number('Quali sono stati i costi? ')
                sale = get_number("A quanto e' stato venduto? ")

                # run the calc function and pass the two values to it
                calc(cost, sale)

        elif int == "v":
            try:
                num1 = float (input("Inserisci la cifra a cui vuoi aggiungere il 40% di marigine: "))
            except:
                print("Devi inserire un numero! ")
            print("Va venduto ad un prezzo netto di euro ", num1 * 1.66666666667)

        else:
            print(
                '--------------------------------------------------------------------------------------------------------------')
            print("Devi inserire o [v] o [m] e premere invio!")













'''''''''
a = 0

while a == 0:
    print("-----------------------------------------------------------------------------------------------------")
    try:
        cost = float(input("Quali sono stati i costi? "))
        sale = float(input("A quanto è stato venduto? "))
    except:
        print("Devi inserire un numero! ")
    if cost > sale:
        print("Nessun margine di guadagno, i costi superano i guadagni! ")
    elif cost == sale:
        print("Sei andato in pari! ")
    elif cost < sale:
        print("Il margine con cui hai venduto è del ",((sale - cost) / sale) * 100, "%")




#post reddit

#! /usr/bin/python
from sys import exit

def error():
    print("Devi scrivere un numero!")

def get_number(question):
    # start the loop and only break out of it if the input given is a number
    while True:
        try:
            cost = float(input(question))
        except ValueError:
            error()
            continue
        except Exception as err:
            print(err)
            exit()

        # just to make sure!
        if isinstance(cost, float):
            break
        else:
            error()
    return cost

def calc(cost, sale):
    if cost > sale:
        print("Nessun margine, hai pagato piu di quanto hai speso! ")
    elif cost == sale:
        print("Sei andato in pari! ")
    elif cost < sale:
        print("Il margine di guadagno e' del ", ((sale - cost) / sale) * 100, "%")

while True:
    # call the get_number function as pass the question to it
    print('--------------------------------------------------------------------------------------------------------------')
    cost = get_number('Quali sono stati i costi? ')
    sale = get_number("A quanto e' stato venduto? ")

    # run the calc function and pass the two values to it
    calc(cost, sale)



   '''''''''
