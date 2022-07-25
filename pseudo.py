from random import randint

print("Tervetuloa kivi sakset paperi peliin tietokonetta vastaan!")
kierrokset = input("Kuinka monta kierrosta haluat pelata?\n")

pelaaja_voitot = 0
tietokone_voitot = 0

for(tee seuraava koodi riippuen kierrokset muutujasta)
    print("Valitse yksi seuraavsita: ")
    print("1. Kivi\n2. Sakset\n3. Paperi")
    pelaaja_valinta = input("Valintasi: ")
    tietokone_valinta = randint(1,3)
    print("Tietokone valitsi:", tietokone_valinta)
    
    if(kaikki tilanteet jolloin pelaaja voittaa)
        print("Voitit kierroksen")
        pelaaja_voitot = pelaaja_voitot + 1
    
    elif(pelaaja_valinta == tietokone_valinta)
        print("Kumpikaan ei saanut pisteitä")
    
    else
        tietokone_voitot = tietokone_voitot + 1
        print("Tietokone voitti kierroksen")
        
    print("Tilanne: Sinä", pelaaja_voitot, "Tietokone", tietokone_voitot)
    
    
if (pelaaja_voitot > tietokone_voitot)
    print("Voitit pelin!:D")

elif (pelaaja_voitot < tietokone_voitot)
    print("Tietokone voitti!")
    
else 
    print("Tasapeli!")
    
