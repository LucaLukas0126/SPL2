zahl 1 = input("Bitte erste Zahl eingeben")
zahl 2 = input("Bitte zweite Zahl eingeben")
zahl 3 = input("Bitte dritte Zahl eingeben")

if(zahl1 < zahl2 < zahl3):
    print( zahl1,zahl2,zahl3)

if(zahl1 < zahl3 < zahl2):
    print( zahl2,zahl3,zahl2)

if(zahl2 < zahl1 < zahl3):
    print( zahl2,zahl1,zahl3)

if(zahl2 < zahl3 < zahl1):
    print( zahl2,zahl3,zahl1)

if(zahl3 < zahl1 < zahl2):
    print( zahl3,zahl1,zahl2)
    
if(zahl3 < zahl2 < zahl1):
    print( zahl3,zahl2,zahl1)