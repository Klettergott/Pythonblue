using System;
[] Zahlen;
class Funktionen
{
        
        def Zahleneingabe()
    {
        string x = Console.ReadLine("eine Zahl: ");
        while '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in x
        {
            try
            {
                float x;
                Zahlen.append(x);
                return;
            }
            catch
            {
                b = Console.ReadLine("moechtest du die bisherige Rechnung durchfuehren? druecke 'a', moechtest du die Zahl erneut eingeben? drueke 'r': ");

                
                if b == 'r'
                {
                    x = input("\neine Zahl: ");
                }
                elif b == 'a'
                {
                    return b;
                }
                else
                {
                    b = input("moechtest du die bisherige Rechnung durchfuehren? druecke 'a', moechtest du die Zahl erneut eingeben? drueke 'r': ");
                    if b == 'a'
                    {
                        return b;
                    }
                }
            }
        }
    }
}
Console.WriteLine(Funktionen.Zahleneingabe())