#beliebige Zahlen in Rechnungen einfügen über Listen
#while input = Zahl fügt die Zahlen solange zur Rechnung hinzu bis man was anderes eingibt
#Liste in Klasse Rechnen eingeben und für die Länge der Liste mit for-schleifen die Rechenoperationen mit den jeweiligen
#Listenindexen(eingegebenen Zahlen) ausführen lassen
#Ergebnis ist eine Variable mit der weitergerechnet werden kann
# (x = input... if '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' in x: x = float(x) else:
#while x not float
class Rechnen:
    def __init__(Za, x, y):
        Za.x = x #for i in Zahlen: Za.float(i) = Zahlen[i]
        Za.y = y #  Zahlen[i]


    def addieren(Za):
        print (f"Ergebnis von {Za.x} + {Za.y} : {Za.x + Za.y}")

    def subtrahieren(Za):
        print(f"Ergebnis von {Za.x} - {Za.y} : {Za.x - Za.y}")

    def multiplizieren(Za):
        print(f"Ergebnis von {Za.x} * {Za.y} : {Za.x * Za.y}")

    def dividieren(Za):
        print (f"Ergebnis von {Za.x} / {Za.y} : {Za.x / Za.y}")

def Zahleneingabe():
        #x = input("\eine Zahl: ")
        #Zahlen = []
        #while '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in x:
            #try:
                #x = float(x)
                #Zahlen.append(x)
                #x = input("eine Zahl?: ")
                #print(Zahlen)
            #except:
                #break
    
        #global z
        #z = Rechnen(Zahlen)
        #for i in Zahlen:
        #   b = b +-*/ Zahlen[i]
        #   
        x, y = float(input("\nerste Zahl: ")), float(input("zweite Zahl: "))
        global z
        z = Rechnen(x, y)

aktiv = True

while aktiv:
    ro = input("""\nwelche Rechenoperation wilst du wählen? \n'1' fuer Addition \n'2' fuer Subtraktion \n'3' fuer Multiplikation
'4' fuer Dividierung \noder irgendwas anderes zum abbrechen: """)
    
    if ro == '1':
        Zahleneingabe()
        z.addieren()
    elif ro == '2':
        Zahleneingabe()
        z.subtrahieren()
    elif ro == '3':
        Zahleneingabe()
        z.multiplizieren()
    elif ro == '4':
        Zahleneingabe()
        z.dividieren()
    else:
        aktiv = False
print("\nTaschenrechner aus")