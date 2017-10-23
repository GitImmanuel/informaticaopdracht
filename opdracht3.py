#Justian Spijkerbosch - justianspijkerbosch.nl - // 23-10-2017.
#Credits naar de goede uitleg over de discriminant methode van: https://wiskundejuffrouw.wordpress.com/2014/04/02/de-abc-formule-2/ (toepassing van https is alleen een beetje mislukt :(.)

#import math
import math

#vragen om de input van de gebruiker (A, B, C) invullen. Zeker er van zijn dat het een cijfer is door het gebruiken van de int() functie.
a = int(input("Vul het bijhorende getal voor A in: "))
b = int(input("Vul het bijhorende getal voor B in: "))
c = int(input("Vul het bijhorende getal voor C in: "))

#basisformule uitrekenen.
basisformule = b*b-4*a*c

#kijken of het een dal of een bergparabool is. Als a kleiner is dan 0 hebben we het over een bergparabool, en anders hebben we het over een dalparabool.
if a < 0:
    parabool = "bergparabool"
else:
    parabool = "dalparabool"

#top berekenen discriminant methode
#als eerst x berekenen door -b / 2 * a, daarna y berekenen met a * (x * x) + b * x + c (formule die opgegeven was.)
topx = (-b) / 2 * a
topy = a * (topx*topx) +  b * topx + c

#als D (basisformule) kleiner is dan 0: Aangeven dat de discriminant geen oplossing heeft.
if basisformule < 0:
    print ("Deze som heeft geen oplossing.")

#als D (basisformule) overeenkomt met het getal 0: Aangeven dat de discriminant één oplossing heeft.
elif basisformule == 0:
    #b negatief maken (-b), + D (basisformule). Gedeeld door 2 * a. Oplossing printen.
    oplossing = (-b+math.sqrt(basisformule)) / 2 * a
    print ("Deze som heeft 1 oplossing: x =", oplossing)
    #aangeven wat van parabool (dal/berg)
    print ("We hebben het over een:", parabool)
    print ("De top is: x =", topx, "y =", topy)

#als D (basisformule) groter is dan 0, aangeven dat er twee oplossingen zijn. Oplossingen printen.
elif basisformule > 0:
    #oplossingeen, b negatief maken, + wortel van D / 2 * a.
    oplossingeen = (-b+math.sqrt(basisformule)) / 2 * a
    #oplossingeen, b negatief maken, - wortel van D / 2 * a. (om beide mogelijkheden te vinden.)
    oplossingtwee = (-b-math.sqrt(basisformule)) / 2 * a
    print ("Deze som heeft 2 oplossingen: x =", oplossingeen, "of: x =", oplossingtwee)
    #aangeven wat van parabool (dal/berg)
    print ("We hebben het over een:", parabool)
    print ("De top is: x =", topx, "y =", topy)