#Justian Spijkerbosch - justianspijkerbosch.nl - // 23-10-2017.

#bedoeling weergeven, en uitleggen voor welk programma welk getal ingevoerd moet worden.
print("Hallo, dit is mijn programma geschreven voor de 4 opdrachten.")
print("Typ 1 voor opdracht 1 & 2, typ 2 voor opdracht 1 & 2. Typ 3 voor opdracht 3 en 4 voor opdracht 4.")

#keuze invoeren
keuze = int(input("Typ je keuze: "))

#kijken wat de keuze is en daarbij het programma (bestand) uitvoeren, in het huidige programma. Dit om de code netjes te houden.
if keuze == 1:
    exec(open("./opdracht1en2.py").read())
elif keuze == 2:
    exec(open("./opdracht1en2.py").read())
elif keuze == 3:
    exec(open("./opdracht3.py").read())
elif keuze == 4:
    exec(open("./opdracht4.py").read())
else:
    print("Dat was niet keuze 1, 2, 3 of 4. Probeer het opnieuw.")
    exec(open("./programma.py").read())