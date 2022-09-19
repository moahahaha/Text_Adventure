from random import randint

liv = randint(3,10)
tau = 0
spade = 0
armer = 2
bein = 2



def start():
    global liv
    global tau
    global spade
    global armer
    global bein

    navn = input("Hei, hva heter du? ")    
    print("Velkommen", navn) 

    asking_navn = True
    while asking_navn == True:
        klar = input("Er du klar for å spille? ja eller nei?  ")

        if klar == "nei":
         asking_name = False
         print("Nei vell")
         exit()

        elif klar == "ja":
         asking_name = False
         print("Du har" , liv, "liv")
         print("Det er en mørk og stormfull aften.")
         print("Du befinner deg alene i en skog")
         print("Plutselig får du øye på en boks")
         print("Hva velger du å gjøre?")
         boks()

        else:
         print("Du skev feil, ingen alternativer heter", klar)


def boks():

    global liv
    global tau
    global spade
    global armer
    global bein

    asking_boks = True
    while asking_boks == True:
      valg = input("a: Gå videre, b: Åpne boksen ")

      if valg == "b":
         asking_boks = False
         print("Inni boksen er det en giftig slange")
         slange()

      elif valg == "a":
        asking_boks = False
        skog()
         
      else:
        print("Du skrev feil, ingen alternativer heter", valg, ". Velg a eller b")

    print("Du har", liv, "liv.") 
    
    skog()


def slange():

    global liv, tau, spade, armer, bein
    
    print("Hva gjør du?")

    asking_slange = True 
    while asking_slange == True:
      slange = input("a: Løp i fra slangen , b: Stirr slangen inn i øynene ")

      if slange == "b":
           asking_slange = False
           print("Du stirret slangen inn i øynene, og den angrep deg. Du mistet 3 liv")
           liv -= 3
           if liv < 1:
             print("Du gikk tom for liv, og døde")
             startpånytt()
           print("Du har", liv, "liv")
           skog()
         

      elif slange == "a":
        asking_slange = False
        print("Du greide å løpe fra slangen")
        skog()
       
      else:
        print("Ugyldig svar avgitt, velg a eller b")


def skog():

   global liv, tau, spade, armer, bein
   
   print("Du fortsetter inn i skogen, og plutselig får du øye på en rød sopp" )
   print("Hva velger du å gjøre?") 

   asking_sopp = True 
   while asking_sopp == True:
     valg = input("a: spis soppen , b: gå videre ")
   
     if valg == "a":
       asking_sopp = False
       print("Du spiste en giftig sopp, og mistet 2 liv")
       liv -= 2 
       if liv < 1:
          print("Du gikk tom for liv og døde")
          startpånytt()
       print("Du har", liv, "liv igjen")
       blåbær()
    
     elif valg == "b":
       asking_sopp = False
       print("Du fortsetter inn i skogen, og fant en spade")
       spade += 1
       rosabær()
    
     else:
        print("Ingen alternativer som heter", valg, "skriv inn a eller b")
     

def blåbær():
  
    global liv, tau, spade, bein, armer
    

    print("Du fortsetter inn i skogen, og snubler over noen blå bær")
    print("Hva velger du å gjøre?")

    asking_blåbær = True
    while asking_blåbær == True:
      valg1 = input("a: spise bærene, b: gå forbi ")

      if valg1 =="a":
          asking_blåbær = False
          print("Bærene var blåbær, og du fikk to liv")
          liv += 2
          print("Du fant også en spade")
          spade += 1
          hull()

      elif valg1 =="b":
          asking_blåbær = False
          print("Du forbi dem, men ble veldig sulten, og mistet 3 liv")
          liv -= 3
          if liv < 1:
              print("Du gikk tom for liv og døde")
              print("Bedre lykke neste gang")
              startpånytt()
          print("Du har", liv, "liv igjen")
          hull()

      else:
        print("Du har ikke skrevet rett, skiv a eller b")


def rosabær():

    global liv, tau, spade, bein, armer
    

    print("Du får øye på noen rosa bær.") 
    print("Hva velger du å gjøre?")

    asking_rosabær = True 
    while asking_rosabær == True:
      valg2 = input("a: Gå forbi bærene, b: Spis bærene ")

      if valg2 == "a":
        asking_rosabær = False
        print("Du gikk forbi bærene, og fant også et tau") 
        tau += 1
        hull()
        
        

      elif valg2 =="b":
        print("Bærene var veldig giftige, og du mistet 5 liv")
        asking_rosabær = False
        liv -= 5
        if liv < 1:
            print("Du gikk tom for liv, og døde av de giftige bærene")
            print("Bedre lykke neste gang")
            startpånytt()
        print("Du har", liv, "liv igjen")
        blåbær()

      else:
        print("Ikke noe alternativ som heter", valg2, ". Velg a eller b")
    

def hull():

    global liv
    global tau
    global spade
    global armer 
    global bein

    print("Du har", liv, "liv,", spade, "spader og", tau, "tau")

    print("Plutselig faller du ned i et dypt mørkt hull")
    
    if tau >= 1:
        tau()
      
    elif spade >= 1:
       spade()
    
    else:
      print("Du hadde ingen tau eller spader til å komme deg opp av hullet med")
      print("Du døde nede i hullet")
      startpånytt()


def tau():

    global liv
    global tau
    global spade
    global armer 
    global bein


    print("Vil du bruke tauet for å komme deg opp av hullet?")

    asking_hull1 = True
    while asking_hull1 == True: 
      hull1 = input("ja, eller nei? ")


      if hull1 == "ja":
        asking_hull1 = False
        print("Du klatret opp av hullet, og fortsetter inn i skogen")
        bjørn()

      elif hull1 == "nei":
        asking_hull1 = False
        print("Du valgte å ikke klatre opp av hullet, og mistet 2 liv av sult")
        liv -= 2
        if liv < 1:
            print("Du døde av sult nede i hullet")
            startpånytt()
        print("Så brukte du tauet til å klatre opp fra hullet likevell")
        tau -= 1
        print("Du har", liv, "liv,", tau, "tau og", spade, "spader.")
        bjørn()

      else:
        print(hull1, "er ikke gyldig. Skriv inn a eller b")


def spade():

    global liv, tau, armer, spade, bein

    print("Vil du bruke en spade å grave deg ut?")

    asking_hull2 = True
    while asking_hull2 == True:
      hull2 = input("ja eller nei? ")

      if hull2 == "ja":
        asking_hull2 = False
        print("Du gravde deg ut av hullet")
        spade -= 1
        bjørn()


      elif hull2 == "nei":
        asking_hull2 = False
        print("Du valgte å ikke grave deg ut, og mistet 2 liv pga. sult")
        liv -= 2
        if liv < 1:
            print("Du døde av sult nede i hullet")
            startpånytt()
        print("Du brukte spaden til å grave deg ut likevell")
        spade -= 1
        print("Du har", liv, "liv,", spade, "spader og", tau, "tau")
        bjørn()

      else:
        print("Svaret", hull2, "er ikke gyldig. Velg alternativ a eller b.") 
    

def bjørn():
    global liv, tau, spade, bein, armer
    
    print("Etter å ha gått en stund til, møter du på en agresiv bjørn.")
    print("Hva gjør du?")

    if tau >= 1:
        tau2()
    
    else:
        no_tau()


    
def tau2():

    global liv, tau, spade, armer, bein

    asking_bjørn1 = True
    while asking_bjørn1 == True:
     bjørn = input("a: løp, b: bruk tauet til å klatre opp i et tre, c: spill død")

     if bjørn == "a":
        asking_bjørn1 = False
        print("Bjørnen var mye raskere enn deg, og tok deg igjen. Den angrep og du mistet 3 liv og et bein")
        print("Dessverre for deg må du nå hinke rundt på et bein")
        liv -= 3
        bein -= 1
        if liv < 1:
            print("Du mistet alle livene i bjørneangrepet og døde.")
            startpånytt()
        print("Du har", liv, "liv,", bein, "bein og", armer, "armer")
        hytte()

     elif bjørn == "b":
        asking_bjørn1 = False
        print("bjørnen klatret opp etter deg i treet, og angrep deg.")
        print("Du mistet 3 liv og en arm")
        liv -= 3
        arm -= 1
        if liv < 1:
            print("Du mistet alle livene dine og døde")
            startpånytt()
        print("Du mistet 3 liv")
        print("Du har", liv, "liv,", bein, "bein og", armer, "arm")
        hytte()

     elif bjørn == "c":
        asking_bjørn1 = False
        print("Du valgte å spille død, og bjørnen gikk forbi deg.")
        hytte()

     else:
        print("Svaret", bjørn, "er ugyldig. Velg alternativ a, b eller c.")
        


def no_tau():

    global liv, tau, spade, armer, bein  
  
    asking_bjørn2 = True
    while asking_bjørn2 == True:
     bjørn2 = input("a: løp, b: spill død, c: hopp på ryggen til bjørnen så den ikke ser deg.")

     if bjørn2 == "a":
        asking_bjørn2 = False
        print("Bjørnen sprang etter deg, og spiste litt på deg")
        print("Du mistet en arm og 2 liv")
        liv -= 2
        armer -= 1
        if liv < 1:
            print("Bjørnen ombestemte seg, og spiste deg helt opp, og du døde")
            print("R.I.P")
            startpånytt()
        print("Du har", liv, "liv og", armer, "armer")
        hytte()
    
     elif bjørn2 == "b":
        asking_bjørn2 = False
        print("Bjørnen syntes du så god ut, og den spiste på deg når du spilte død")
        print("Du mistet 2 liv og et bein")
        liv -= 2
        bein -= 1
        if liv < 1:
            print("Bjørnen spiste deg helt opp, og du døde.")
            startpånytt()
        print("Du har", liv, "liv og", bein, "bein, og må nå dessverre hinke rundt")
        hytte()

     elif bjørn2 == "c":
        asking_bjørn2 = False
        print("Bjørnen ble redd, og sprang rundt, og du datt av i en myk busk") 
        hytte()

     else:
        print("Svaret", bjørn2, "er ikke gyldig. Skriv inn a, b eller c.")



def hytte():
    global liv, tau, spade, armer, bein  
  

def startpånytt():
    asking_start = True
    while asking_start == True:
     valg = input("Vil du starte på nytt?")

     if valg == "ja":
        asking_start = False
        start()
    
     elif valg == "nei":
        asking_start = False
        print("Ok.")
        exit()
    
     else:
        print("Ugyldig svar avgitt. Svar ja eller nei")



start()