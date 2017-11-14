#Justian Spijkerbosch - justianspijkerbosch.nl - // 23-10-2017.

#begintekst (Hallo zeggen, bedoeling uitleggen vragen om de gegevens.)
print("Hallo met deze applicatie kunt u het alcoholpromillage in uw bloed, en uw toestand berekenen. Na het drinken van een paar biertjes.")
print("Als eerst hebben we een paar gegevens nodig, deze gaan we nu verzamelen.")

#gegevens vragen en er een variable aan vast zetten.
gewicht = input("Wat is uw gewicht (in kg): ")
glazen = input("Hoeveel glazen bier heeft u gedronken: ")
geslacht = input("Bent u een man of vrouw antwoord met m of v of man of vrouw: ")
uur = input("Hoeveel uur geleden dronk u het eerste glas: ")

#nagaan of geslacht vrouw/man is, rekengedeelte koppelen.
if geslacht == "man" or geslacht == "m":
    rekengedeelte = 0.7
elif geslacht == "vrouw" or geslacht == "v":
    rekengedeelte = 0.5
else: 
    print("Dat is geen goede input.")

#rekenen
som = ((int(glazen) * 10) / (int(gewicht) * rekengedeelte)) - (int(uur) - 0.5) * (int(gewicht) * 0.002)

#toestanden binden aan het som van promillage.
if som < 0.5:
    toestand = "opgewekt"
elif som >= 0.5 and som < 1.5:
    toestand = "aangeschoten"
elif som >= 1.5 and som < 3.0:
    toestand = "zat"
elif som >= 3.0 and som < 4.0:
    toestand = "ladderzat"
elif som >= 4.0:
    toestand = "Laveloos, voor pampus"

#rijtoestand binden aan het som van promillage
if som < 0.5:
    rijtoestand = "U mag rijden."
else:
    rijtoestand = "Het is te hoog ga niet meer achter het stuur als dit te hoog is!"

#alcoholpromillage weergeven + toestand.
print("Uw alcoholpromillage is:", round(som), "Uw toestand is:", toestand)
#opdracht 2 deel = rijtoestand weergeven.
print("Uw rijtoestand is:", rijtoestand)

#opdracht2
print("Zolang het alcoholpromillage onder de 0.5 is mag er nog worden gereden, uw toestand wordt hierboven gezegd en als u nog mag rijden wordt dat er aangegeven.")
print("Je mag nog met 2 biertjes rijden, met 3 niet meer volgens de berekening.")
print("Met twintig biertjes moet je langer dan 30 uur wachten.")


    

