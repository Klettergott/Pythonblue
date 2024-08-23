using System;

[] Zahlen;
class Funktionen
{
        
        def Zahleneingabe()
    {
        string x = Console.ReadLine("eine Zahl: ");
        while ('0' || '1' || '2' || '3' || '4' || '5' || '6' || '7' || '8' || '9' in x)
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
Funktionen.Zahleneingabe();
Console.WriteLine("Hello there")
Console.ReadLine()