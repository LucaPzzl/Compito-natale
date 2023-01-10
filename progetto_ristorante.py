import random

prenotazioni=[]

menu1="\nPrimi piatti:\n 1)Speghetti allo scoglio\n 2)Lasagna\n 3)Carbonara\n"
menu2="Secondi piatti:\n 4)Grigliata mista di carne\n 5)Polpette\n 6)Salmone alla griglia\n"
menu3="Dolci:\n 7)Tenerina\n 8)Mascarpone\n 9)Torta alle mele\n"
menu4="Bevande:\n 10)Acqua\n 11)Fanta\n 12)Gassosa\n 13)Té al limone\n"

menu_prezzi={"1":12,"2":13,"3":16,"4":24,"5":12,"6":16,"7":13,"8":14,"9":11,"10":1,"11":2,"12":2,"13":2}
id_nome={"1":"Speghetti allo scoglio","2":"Lasagna","3":"Carbonara","4":"Grigliata mista di carne","5":"Polpette","6":"Salmone alla griglia","7":"Tenerina","8":"Mascarpone","9":"Torta alle mele","10":"Acqua","11":"Fanta","12":"Gassosa","13":"Té al limone"}

camerieri={"Carlo_Rossi":12, "Piero_Bianchi":5, "Naldo_Verdi":1, "Piero_Rossi":1}
while True:
    tavoli=20
    tavoli_occ=[]
    prenotazione=[]
    while True:
        scelta1=input("Clienti al telefono per prenotazione? ")
        if scelta1=="sì":
            prenota_g=input("Per quale giorno vuole prenotare? ")
            prenotazione.append(prenota_g)
            
            prenota_o=input("Per quale ora? ")
            prenotazione.append(prenota_o)
            
            prenota_n=input("Per quante persone? ")
            prenotazione.append(prenota_n)

            prenota_f=input("Fumate? ")
            prenotazione.append(prenota_f)

            prenota_t=input("Il suo numero di telefono ")
            prenotazione.append(prenota_t)

            prenota_n=input("Il suo nome ")
            prenotazione.append(prenota_n)

            while True:
                tavolo=random.randint(0,tavoli)
                if tavolo in tavoli_occ:
                    tavolo=random.randint(0,tavoli)
                    break
                else:
                    tavoli_occ.append(tavolo)
                    break
            tavoli-=1
            print("Grazie, arrivederci\n")
            
        else:
            prenota=input("Avete prenotato? ")
            scontrino=""
            if prenota=="sì":
                nome_cliente=input("A che nome è la prenotazione? ")
                i=0
                for i in prenotazioni:
                    for nome in i:
                        if nome==nome_cliente:
                            print("Prego, accomodatevi\n ")
                            print(menu1)
                            print(menu2)
                            print(menu3)
                            print(menu4)
                            conto=0
                            while True:
                                richiesta=input("Cosa desidera? ")
                                if richiesta!="no":
                                    conto+=menu_prezzi[richiesta]
                                    scontrino+="-"
                                    scontrino+=str(id_nome[richiesta])
                                    scontrino+=": "
                                    scontrino+=str(menu_prezzi[richiesta])
                                    scontrino+=" €"
                                    scontrino+="\n"
                                else:
                                    print("Scontrino\n")
                                    print("Ecco il suo conto:\n",scontrino,conto," €")
                                    break
                            break
        
            else:
                print("Non avete prenotato, verifichiamo se ci sono tavoli liberi")
                scontrino=""
                if tavoli>0:
                    x=random.randint(0,tavoli)
                    if x in tavoli_occ:
                        x=random.randint(0,tavoli)
                                    
                    else:  
                        print("Prego accomodatevi al tavolo numero ",x)
                        print(menu1)
                        print(menu2)
                        print(menu3)
                        print(menu4)
                        conto=0
                        while True:
                                richiesta=input("Cosa desidera? ")
                                if richiesta!="no":
                                    conto+=menu_prezzi[richiesta]
                                    scontrino+="-"
                                    scontrino+=str(id_nome[richiesta])
                                    scontrino+=": "
                                    scontrino+=str(menu_prezzi[richiesta])
                                    scontrino+=" €"
                                    scontrino+="\n"
                                else:
                                    print("Scontrino\n")
                                    print("Ecco il suo conto:\n",scontrino)
                                    print("Totale: ",conto," €")
                                    break
                        break
                            
                else:
                    print("Tutti i tavoli sono occupati")
                    break

        prenotazioni.append(prenotazione)
        


