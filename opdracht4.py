#Justian Spijkerbosch - justianspijkerbosch.nl - // 23-10-2017.

#import de math (wiskunde) module.
import math

#creert een functie met de naam opdracht4 waardoor de functie gecalled kan worden met opdracht4().
def opdracht4():
    #loopt als eerst over de zijde A heen, tussen de 1 en 1000. Daarna zijde B en daarna zijde C (het antwoord). Hij gaat alle mogelijkheden tussen de 1 en 1000 in alle gevallen na, van elke zijde. door het gebruik van de range() functie kunnen er geen kommagetallen oid voorkomen.
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                #nagaan of c*c (kwadrateren met zich zelf), gelijkstaat (schuine zijde) aan a*a (rechte zijde) + b*b (rechte zijde). Door het gebruik van de range() functie komen er geen wortels, breuken, kommagetalen oid voor als input.)
                if c*c == a*a + b*b and a + b + c == 1000:                  
                    print (a, b, c)

#called de functie om ook daadwerkelijk de code in zijn werking te zetten, en het resultaat uiteindelijk weer te geven.
opdracht4()

