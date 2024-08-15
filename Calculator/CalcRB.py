#Taschenrechner mit unbegrenzter Recheneingabe


def Zahleneingabe():
        x = input("\neine Zahl: ")
        while '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in x:
           
            try:
                x = float(x)
                Zahlen.append(x)
                return
            except:
                global b
                b = input("""\nmoechtest du die bisherige Rechnung durchfuehren? druecke 'a'
moechtest du die Zahl erneut eingeben? drueke 'r' \nmoechtest du den Rechenvorgang abbrechen? druecke 'e'\n""")
                
                if b == 'r':
                    x = input("\neine Zahl: ")
                elif b == 'e':
                    aktiv = False
                    return aktiv
                elif b == 'a':
                    return b
                else:
                    b = input("""\nmoechtest du die bisherige Rechnung durchfuehren? druecke 'a'
moechtest du die Zahl erneut eingeben? drueke 'r' \nmoechtest du den Rechenvorgang abbrechen? druecke 'e'\n""")
                    if b == 'a':
                        return b
    

def Rechenoperation():
    if len(r_operationen) > 0:
        ro = input("Rechenoperation?: ")
    else:
        ro = input("""\nwelche Rechenoperation wilst du wählen? \n'+' fuer Addition \n'-' fuer Subtraktion \n'*' fuer Multiplikation
'/' fuer Dividierung \netwas anderes fuer weitere Optionen: """)
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
            b = input("""\nwillst du die bisherige Rechnung ausfuehren? druecke 'a'
willst du erneut versuchen eine Rechenoperation zu waehlen? druecke 'r' \nwillst du den Rechenvorgang abbrechen? druecke 'e' : """)
            if b == 'a':
                return b
            elif b == 'r':
                ro = input("""\nwelche Rechenoperation wilst du wählen? \n'+' fuer Addition \n'-' fuer Subtraktion \n'*' fuer Multiplikation
'/' fuer Dividierung \netwas anderes fuer weitere Optionen: """)
            elif b == 'e':
                aktiv = False
                return aktiv
            else:
                print("Jetzt gib mal was vernuenftiges ein Kollege Schnuerschuh!")
                b = input("""\nwillst du die bisherige Rechnung ausfuehren? druecke 'a'
willst du erneut versuchen eine Rechenoperation zu waehlen? druecke 'r' \nwillst du den Rechenvorgang abbrechen? druecke 'e' : """)
                if b == 'a':
                    return b
            


def Rechnung():
    global Ergebnis
    global Rechenweg
    Ergebnis = [0]
    Rechenweg = []
    for i in range(len(Zahlen)):
      try:
        if r_operationen[i] == '+':
            try:
                Rechenweg.append(Ergebnis[0], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] + Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Zahlen[i] + Zahlen[i + 1]

        elif r_operationen[i] == '-':
            try:
                Rechenweg.append(Ergebnis[0], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] - Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Zahlen[i] - Zahlen[i + 1]

        elif r_operationen[i] == '*':
            try:
                Rechenweg.append(Ergebnis[0], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] * Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Zahlen[i] * Zahlen[i + 1]
        elif r_operationen[i] == '/':
            try:
                Rechenweg.append(Ergebnis[0], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Ergebnis[0] / Zahlen[i + 1]
            except:
                Rechenweg.append(Zahlen[i], r_operationen[i], Zahlen[i + 1])
                Ergebnis[0] = Zahlen[i] / Zahlen[i + 1]
      except:
          print(f"\nDie Rechnung: {Rechenweg}")
          print(f"Dein Endergebnis: {Ergebnis[0]}\n\n")



def Taschenrechner():
    global aktiv
    global r_operationen
    global b
    global Zahlen
    aktiv = True
    r_operationen = []
    b = 'l'
    Zahlen = []

    while aktiv:

        while b != 'a':
            Zahleneingabe()
            Rechenoperation()
        
        Rechnung()
        Rechenweg.clear
        Ergebnis.clear
        b = 'reset'
    print("Taschenrechner aus.")

Taschenrechner()