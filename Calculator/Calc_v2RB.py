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
                    elif b == 'r':
                        x = input("\neine Zahl: ")
    

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
    for i in range(len(r_operationen)):
        Rechenweg.append(Zahlen[i]), Rechenweg.append(r_operationen[i])
        if i == len(r_operationen) - 1:
            if len(Zahlen) > len(r_operationen):
                Rechenweg.append(Zahlen[i + 1])
            else:
                Rechenweg.pop()


    """ Hauptproblem ist noch, dass wenn man - 12 * 12 * 12 rechnen würde, nicht die Vorzeichen Vergabe mit beim Verrechnen ins Endergebnis
    berücksichtigt wird, sondern erstmal Ergebnis[0] -= 12 * 12 hinzugefügt wird und dann Ergebnis[0] += 12 * 12 im Anschluss draufgerechnet wird
    # Ich vermute man brauch eine andere Hinzufügungsmethode statt Ergebnis[0] +/-= Rechnung, eventuell mit 
    # mehreren zwischenergebnissen, die am Ende des Rechenweges zusammengeführt werden.
    # vielleicht wenn + oder - auftaucht und danach nur Operatoren wie * und / folgen solange die nächsten Sachen verrechnen, bis als nächster Rechenoperator
    # wieder ein + oder - auftaucht oder der Rechenweg ein Ende hat und im Anschluss zum Ergebnis hinzufügen mit jeweiligem Vorzeichen  """

    #wenn kein Plus Minus davor steht einzeln multiplizieren/dividieren, ansonsten auslassen
    for i in range(len(Rechenweg)):
        try:
            if Rechenweg[i] == '/' and Rechenweg[i - 2] != '-' and Rechenweg[i - 2] != '+':
                Ergebnis[0] += Rechenweg[i - 1] / Rechenweg[i + 1]
            elif Rechenweg[i] == '/' and Rechenweg[i - 2] == '-':
                continue
            elif Rechenweg[i] == '/' and Rechenweg[i - 2] == '+':
                continue

            elif Rechenweg[i] == '*' and Rechenweg[i - 2] != '-' and Rechenweg[i - 2] != '+':
                Ergebnis[0] += Rechenweg[i - 1] * Rechenweg[i + 1]
            elif Rechenweg[i] == '*' and Rechenweg[i - 2] == '-':
                continue
            elif Rechenweg[i] == '*' and Rechenweg[i - 2] == '+':
                continue
        except:
            try:
                if Rechenweg[i] == '/' and Rechenweg[i - 2] == '/':
                    Ergebnis[0] /= Rechenweg[i + 1]
                elif Rechenweg[i] == '/' and Rechenweg[i - 2] == '*':
                    Ergebnis[0] /= Rechenweg[i + 1]

                elif Rechenweg[i] == '*' and Rechenweg[i - 2] == '/':
                    Ergebnis[0] *= Rechenweg[i + 1]
                elif Rechenweg[i] == '*' and Rechenweg[i - 2] == '*':
                    Ergebnis[0] *= Rechenweg[i + 1]
            except:
                if Rechenweg[i] == '/':
                    Ergebnis[0] += Rechenweg[i - 1] / Rechenweg[i + 1]

                elif Rechenweg[i] == '*':
                    Ergebnis[0] += Rechenweg[i - 1] * Rechenweg[i + 1]
                continue

        #Plus Minus erkennen und zuerst multiplizieren/dividieren
        try:
            if Rechenweg[i] == '+' and Rechenweg[i + 2] == '/':
                Ergebnis[0] += Rechenweg[i + 1] / Rechenweg[i + 3]

            elif Rechenweg[i] == '+' and Rechenweg[i + 2] == '*':
                Ergebnis[0] += Rechenweg[i + 1] * Rechenweg[i + 3]
        except:
            if Rechenweg[i] == '+':
                Ergebnis[0] += Rechenweg[i + 1]
            continue

        try:
            if Rechenweg[i] == '-' and Rechenweg[i + 2] == '/':
                Ergebnis[0] -= Rechenweg[i + 1] / Rechenweg[i + 3]

            elif Rechenweg[i] == '-' and Rechenweg[i + 2] == '*':
                Ergebnis[0] -= Rechenweg[i + 1] * Rechenweg[i + 3]

        except:
            if Rechenweg[i] == '-':
                Ergebnis[0] -= Rechenweg[i + 1]
            continue


    print(f"\nDie Rechnung: {Rechenweg}")
    print(f"Dein Endergebnis: {Ergebnis} {sum(Ergebnis)}\n\n")



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
    Ergebnis = [0]
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

'''
pow(x, y) function = x ^ y
'''

'''
math module:
math.pow(x, y) x hoch y
math.sqrt(x) = Wurzel aus x
'''