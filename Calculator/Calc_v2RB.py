#Taschenrechner mit mehrfacheingabe
#fehlt Punkt vor Strich Rechnung
#GUI
#Rechenausgabe bei Zahleingabenabbruch statt weiterleitung zu Rechenoperatoren
#umgang mit den globalen Variablen. Hauptsächlich b wegen der while-Schleife in Funktion Taschenrechner()

def Zahleneingabe():
        x = input("eine Zahl: ")
        while '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in x:
           
            try:
                x = float(x)
                Zahlen.append(x)
                return
            except:
                b = input("""\nmoechtest du die bisherige Rechnung durchfuehren? druecke 'a'
moechtest du die Zahl erneut eingeben? drueke 'r' \n""")
                
                if b == 'r':
                    x = input("\neine Zahl: ")
                elif b == 'a':
                    return b
                else:
                    b = input("""\nmoechtest du die bisherige Rechnung durchfuehren? druecke 'a'
moechtest du die Zahl erneut eingeben? drueke 'r' \n""")
                    if b == 'a':
                        return b
    

def Rechenoperation():
    if len(r_operationen) > 0:
        ro = input("Rechenoperation?: ")
    else:
        ro = input("""\nwelche Rechenoperation wilst du wählen? \n'+' fuer Addition \n'-' fuer Subtraktion \n'*' fuer Multiplikation
'/' fuer Dividierung \netwas anderes fuer weitere Optionen: \n""")
    while len(ro) > 0:
        if ro == '+':
            r_operationen.append("+")
            return
        elif ro == '-':
            r_operationen.append("-")
            return
        elif ro == '*':
            r_operationen.append("*")
            return
        elif ro == '/':
            r_operationen.append("/")
            return
        else:
            global b
            b = input("""\nwillst du die bisherige Rechnung ausfuehren? druecke 'a'
willst du erneut versuchen eine Rechenoperation zu waehlen? druecke 'r' \n""")
            if b == 'a':
                return
            elif b == 'r':
                ro = input("""\nwelche Rechenoperation wilst du wählen? \n'+' fuer Addition \n'-' fuer Subtraktion \n'*' fuer Multiplikation
'/' fuer Dividierung \netwas anderes fuer weitere Optionen: \n""")
            else:
                print("Jetzt gib mal was vernuenftiges ein Kollege Schnuerschuh!")
                b = input("""\nwillst du die bisherige Rechnung ausfuehren? druecke 'a'
willst du erneut versuchen eine Rechenoperation zu waehlen? druecke 'r' \n""")
                if b == 'a':
                    return
            


def Rechnung():
    for i in range(len(Zahlen) - 1):
        if r_operationen[i] == '+':
            try:
                Rechenweg.append(Ergebnis[0]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] + Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis.append(Zahlen[i] + Zahlen[i + 1])

        elif r_operationen[i] == '-':
            try:
                Rechenweg.append(Ergebnis[0]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] - Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis.append(Zahlen[i] - Zahlen[i + 1])

        elif r_operationen[i] == '*':
            try:
                Rechenweg.append(Ergebnis[0]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] * Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis.append(Zahlen[i] * Zahlen[i + 1])
        elif r_operationen[i] == '/':
            try:
                Rechenweg.append(Ergebnis[0]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] / Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
                Ergebnis.append(Zahlen[i] / Zahlen[i + 1])

    print(f"\nDie Rechnung: {Rechenweg}")
    print(f"Dein Endergebnis: {Ergebnis}\n\n")



def Taschenrechner():
    global aktiv
    global r_operationen
    global b
    global Zahlen
    global Ergebnis
    global Rechenweg
    aktiv = True
    r_operationen = []
    b = 'l'
    Zahlen = []
    Ergebnis = []
    Rechenweg = []

    while aktiv:

        while b != 'a':
            if Zahleneingabe() == 'a':
                break
            Rechenoperation()
        
        Rechnung()

        z = input("Taschenrechner ausmachen? druecke 'e' \netwas anderes um fortzufahren: ")
        if z == 'e':
            aktiv = False
        else:
            b = 'reset'
            Rechenweg = []
            Ergebnis = []
            r_operationen = []
            Zahlen = []
            print("\nNeue Rechnung: \n")
    print("\nTaschenrechner aus.\n")

Taschenrechner()

#Funktion fuer Punkt vor Strich Rechnung:
'''
for i in range(len(Zahlen) - 1):
    Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i]), Rechenweg.append(Zahlen[i + 1])
for i in range(len(Rechenweg)):
    if '/' in Rechenweg[i]:
        try:
            Ergebnis[0] = Rechenweg[i - 1] / Rechenweg[i + 1]
            Rechenweg.insert(i + 2, Ergebnis[0])
        except:
            continue
    if '*' in Rechenweg[i]:
        try:
            Ergebnis[0] = Rechenweg[i - 1] * Rechenweg[i + 1]
            Rechenweg.insert(i + 2, Ergebnis[0])
        except:
            continue
'''