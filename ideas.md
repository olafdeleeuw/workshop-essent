### daylight savings

####

1. Function that accepts different timestamp formats from csv and converts it into a standard DateTimeIndex
2. Input default local time
3. Output default UTC
4. We would like to have a function that converts to timezone of choice
5. Read function must have a parameter timezone so user can say which timezone it is.
6. Functie die checkt of een uur mist bij daylight savings en dit extrapoleert en in maart verwijderd.
7. Functie die checkt of daylight savings op juiste tijdstip is toegepast. Zo niet: terugschuiven
8. Functie die rest van timeseries checkt en een percentage geeft van aantal missende uren.
9. De read csv functie moet de timestamp column sorteren
10. Goede controle op voledigheid van timeseries --> fouten als warning

[//]: # (5. If user didn't put a timezone in read function we have a function that tries to figure out if it is UTC. )