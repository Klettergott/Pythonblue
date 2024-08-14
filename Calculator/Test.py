'''
print("Flugzeug\nLandebahn")
i = input()
i = float(i)
print(i+i)
'''

x = input("\neine Zahl?: ")
Zahlen = []
while '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in x:
    try:
        x = float(x)
        Zahlen.append(x)
        x = input("\neine Zahl?: ")
        print(Zahlen)
    except:
        break
    