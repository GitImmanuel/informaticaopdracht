#Justian Spijkerbosch - justianspijkerbosch.nl - // 23-10-2017.

#begintekst (Hallo zeggen, bedoeling uitleggen vragen om de gegevens.)
print("Hallo met deze applicatie kunt u het alcoholpromillage in uw bloed, en uw toestand berekenen. Na het drinken van een paar biertjes.")
print("Als eerst hebben we een paar gegevens nodig, deze gaan we nu verzamelen.")

#gegevens vragen en er een variable aan vast zetten.
gewicht = input("Wat is uw gewicht (in kg): ")
glazen = input("Hoeveel glazen bier heeft u gedronken: ")
geslacht = input("Bent u een man of vrouw antwoord met m of v of man of vrouw: ")
uur = input("Hoeveel uur geleden dronk u het eerste glas: ")

#a * 10 uitrekenen. Variable Alcoholpro aanvast zetten.
alcoholpro = int(glazen) * 10
#(u - 0.5) uitrekenen. Variable uren aanvast zetten.
uren = int(uur) - 0.5
#(g * 0.002) uitrekenen. Variable kilo aanvast zetten.
kilo = int(gewicht) * 0.002

#tweede deel van de totale formule (uren * kilo) uitrekenen.
deeltwee = uren * kilo

#deel van de code voor mannen, maat voor lichaamsvocht vastgezet op 0.7
if geslacht == "m" or "man":
    #andere deel van de formule uitrekenen (alcoholpro (hierboven) / gewicht * 0.7 (g * r in de formule.))
    deeleenman = int(alcoholpro) / int(gewicht) * 0.7
    #eindresultaat uitrekenen (deel een van de formule - deel twee)
    resultaatzondermath = int(deeleenman) - int(deeltwee)
    #variable resultaat gelijkzetten aan resultaatzondermath
    resultaat = resultaatzondermath

#deel van de code voor vrouwen, maat voor lichaamsvocht vastgezet op 0.5
elif geslacht == "v" or "vrouw":
    #andere deel van de formule uitrekenen (alcoholpro (hierboven) / gewicht * 0.5 (g * r in de formule.))
    deeleenvrouw = int(alcoholpro) / int(gewicht) * 0.5
    #eindresultaat uitrekenen (deel een van de formule - deel twee)
    resultaatzondermath = int(deeleenvrouw) - int(deeltwee)
    #variable resultaat gelijkzetten aan resultaatzondermath
    resultaat = resultaatzondermath

#toestanden binden aan het resultaat van promillage.
if resultaat < 0.5:
    toestand = "opgewekt"

elif resultaat >= 0.5 and resultaat < 1.5:
    toestand = "aangeschoten"

elif resultaat >= 1.5 and resultaat < 3.0:
    toestand = "zat"

elif resultaat >= 3.0 and resultaat < 4.0:
    toestand = "ladderzat"

elif resultaat >= 4.0:
    toestand = "Laveloos, voor pampus"

#rijtoestand binden aan het resultaat van promillage
if resultaat < 0.5:
    rijtoestand = "U mag rijden."

else:
    rijtoestand = "Het is te hoog ga niet meer achter het stuur als dit te hoog is!"

#alcoholpromillage weergeven + toestand.
print("Uw alcoholpromillage is:", resultaat, "Uw toestand is:", toestand)
#opdracht 2 deel = rijtoestand weergeven.
print("Uw rijtoestand is:", rijtoestand)

