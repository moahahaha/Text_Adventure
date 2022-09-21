from operator import __truediv__
from random import randint



tau = 0
spade = 0
armer = 2
bein = 2
brødskive = 0
liv = randint(3,10)
    
    
def start():

    global spade, armer, bein, brødskive, liv

    if liv < 1:
      liv = randint(3,10)
   
    navn = input("Hei, hva heter du? ")    
    print("Velkommen", navn) 

    asking_navn = True
    while asking_navn == True:
        klar = input("Er du klar for å spille? ja eller nei?  ")

        if klar == "nei":
         asking_navn = False
         print("Nei vell")
         startpånytt()

        elif klar == "ja":
         asking_navn = False
         print("Du har" , liv, "liv")
         print("Det er en mørk og stormfull aften.")
         print("Du befinner deg alene i en skog")
         print("Plutselig får du øye på en boks")
         print("Hva velger du å gjøre?")
         boks()

        else:
         print("Du skev feil, ingen alternativer heter", klar)


def boks():

    global liv, tau, spade, armer, bein

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
        tau += 1 
        print("Du fikk et tau")
        print("Du har", liv, "liv,", spade, "spader og", tau, "tau.")
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
       print("Du fortsetter inn i skogen")
       rosabaer()
    
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


def rosabaer():

    global liv, tau, spade, bein, armer
    

    print("Du får øye på noen rosa bær.") 
    print("Hva velger du å gjøre?")

    asking_rosabaer = True 
    while asking_rosabaer == True:
      valg2 = input("a: Gå forbi bærene, b: Spis bærene ")

      if valg2 == "a":
        asking_rosabaer = False
        print("Du gikk forbi bærene, og fant også et tau") 
        tau += 1
        hull()
        
        

      elif valg2 =="b":
        print("Bærene var veldig giftige, og du mistet 5 liv")
        asking_rosabaer = False
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

    global liv, tau, spade, armer, bein

    print("Du har", liv, "liv,", spade, "spader og", tau, "tau")

    print("Plutselig faller du ned i et dypt mørkt hull")
    
    if tau >= 1:
        tau_()
      
    elif spade >= 1:
       spade_()
    
    else:
      print("Du hadde ingen tau eller spader til å komme deg opp av hullet med")
      print("Du døde nede i hullet")
      startpånytt()


def tau_():

    global liv, tau, spade, armer, bein

    print("Vil du bruke tauet for å komme deg opp av hullet?")

    asking_hull1 = True
    while asking_hull1 == True: 
      hull1 = input("ja, eller nei? ")


      if hull1 == "ja":
        asking_hull1 = False
        print("Du klatret opp av hullet, og fortsetter inn i skogen")
        tau -= 1
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


def spade_():

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
     bjørn = input("a: løp, b: bruk tauet til å klatre opp i et tre, c: spill død ")

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
        armer -= 1
        if liv < 1:
            print("Du mistet alle livene dine og døde")
            startpånytt()
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
    print("Du fortsetter å vandre rundt i skogen, og får plutselig øye på en rød hytte.")
    print("Du tenker du kanskje kan finne noe mat inne der, og går inn i hytta.")
    gang()


def gang():
  print("Du står nå i gangen.")
  print("Foran deg har du 2 dører, en rød og en blå.")
  asking_gang = True
  while asking_gang == True:
    valg_gang = input("Hvilken dør velger du? rød eller blå? ")

    if valg_gang == "rød":
      asking_gang = False
      stue()

    elif valg_gang == "blå":
      asking_gang = False
      soverom1()

    else:
      print("Svar ikke gyldig. venligst skiv inn rød eller blå")
    

def stue():
   print("Du står nå i stua.")
   print("Foran deg er det 4 dører. En gul, en rød, en lyserød, og en mørkegrønn")
   asking_stue = True
   while asking_stue == True:
    valg_stue = input("Hvilken dør velger du? gul, rød, lyserød eller mørkegrønn? ")

    if valg_stue == "gul":
      asking_stue = False
      bad2()
      
    
    elif valg_stue == "rød":
      asking_stue = False
      gang()

    elif valg_stue == "mørkegrønn":
      asking_stue = False
      bad()
    
    elif valg_stue == "lyserød":
      asking_stue = False
      kjeller()

    else:
      print("Ugyldig svar avgitt, skriv inn gul, rød, eller grønn")


def soverom1():
    print("Du står nå i soverom 1")
    print("Foran deg er det 3 dører, en blå, en lysegrønn og en grønn")
    asking_soverom1 = True
    while asking_soverom1 == True:
     valg_soverom1 = input("Hvilken dør velger du? blå, lysegrønn eller grønn? ")

     if valg_soverom1 == "blå":
      asking_soverom1 = False
      gang()
    
     elif valg_soverom1 == "grønn":
      asking_soverom1 = False
      bad()

     elif valg_soverom1 == "lysegrønn":
      vaskerom()

     else:
      print("Svaret er ikke gyldig. Prøv å skriv inn blå eller grønn")

    
def bad():
  print("Du står nå på bad 1")
  print("Foran deg har du 3 dører, en grønn, en mørkegrønn, og en oransje")
  asking_bad = True 
  while asking_bad == True:
    valg_bad = input("Hvilken dør velger du? grønn, mørkegrønn eller oransje? ")

    if valg_bad == "grønn":
      asking_bad = False
      soverom1()

    elif valg_bad == "mørkegrønn":
      asking_bad = False
      stue()
    
    elif valg_bad == "oransje":
      asking_bad = False
      bad2()

    else:
      print("Ingen svar som heter", valg_bad, ". Skriv inn et av alternativene.")


def kjeller():
  print("Du står nå i kjelleren")
  print("Foran deg er det 3 dører. En lyserød, en lilla og en turkis")
  asking_kjeller = True 
  while asking_kjeller == True:
    valg_kjeller = input("Hvilken dør velger du? ")

    if valg_kjeller == "lyserød":
      asking_kjeller = False
      stue()

    elif valg_kjeller == "lilla":
      asking_kjeller = False 
      bod()

    elif valg_kjeller == "turkis":
      asking_kjeller = False
      trapp()

    else:
      print("Svar ikke gyldig. Skriv inn lyserød, lilla eller tuskis ")
    

def bad2():
  print("Du står nå på bad 2")
  print("Foran deg er det 2 dører, en oransje, og en gul")
  asking_bad2 = True 
  while asking_bad2 == True:
    valg_bad2 = input("Hvilken dør velger du? oransje eller gul? ")

    if valg_bad2 == "oransje":
      asking_bad2 = False
      bad()

    elif valg_bad2 == "gul":
      asking_bad2 = False
      stue()

    else:
      print("Ingen alternativer som heter", valg_bad2, ". Prøv på nytt.")


def bod():
  print("Du står nå i boden.")
  print("Foran deg har du 2 dører, en purpur, og en lilla.")
  asking_bod = True
  while asking_bod == True:
    valg_bod = input("Hvilken dør velger du? purpur eller lilla? ")

    if valg_bod == "lilla":
      asking_bod = False 
      kjeller()

    elif valg_bod == "purpur":
      
      asking_bod = False 
      trapp()

    else:
      print("Det er ingen alternativer som heter", valg_bod, ". Skriv inn purpur eller lilla")

    
def trapp():
  print("Du står nå i trappen.")
  print("Forran deg er det 3 dører. En turkis, en brun, og en purpur")
  asking_trapp = True
  while asking_trapp == True:
    valg_trapp = input("Hvilken dør vil du velge? ")

    if valg_trapp == "turkis":
      asking_trapp = False
      kjeller()

    elif valg_trapp == "brun":
      asking_trapp = False 
      loft()

    elif valg_trapp == "purpur":
      asking_trapp = False
      bod()

    else:
      print(valg_trapp, "er ikke gyldig. Prøv på nytt")


def vaskerom():
  print("Du står nå på vaskerommet")
  print("Foran deg er det 3 dører. En grå, en lysegrønn og en fiolett")
  asking_vaskerom = True 
  while asking_vaskerom == True:
    valg_vaskerom = input("Hvilken dør velger du? ")

    if valg_vaskerom == "grå":
      asking_vaskerom = False 
      roterom()

    elif valg_vaskerom == "lysegrønn":
      asking_vaskerom = False 
      soverom1()

    elif valg_vaskerom == "fiolett":
      asking_vaskerom = False
      soverom2()

    else:
      print(valg_vaskerom, "er ikk et gyldig svar. Prøv på nytt")


def loft():
  print("Du står nå på loftet")
  print("Foran deg er det 3 dører. En brun, en svart, og en hvit")
  asking_loft = True
  while asking_loft == True:
    valg_loft = input("Hvilken dør vil du velge? brun, svart eller hvit? ")

    if valg_loft == "brun":
      asking_loft = False 
      trapp()

    elif valg_loft == "svart":
      asking_loft = False
      trapp2()

    elif valg_loft == "hvit":
      asking_loft = False
      roterom()

    else:
      print("Svaret", valg_loft, "er ikke gyldig. Prøv på nytt.")


def roterom():
  print("Du står nå inne på roterommet")
  print("Foran deg har du 2 dører, en hvit, og en grå.")
  asking_roterom = True
  while asking_roterom == True:
    valg_roterom = input("Vil du gå inn hvit eller grå dør? ")

    if valg_roterom == "hvit":
      asking_roterom = False
      loft()

    elif valg_roterom == "grå":
      asking_roterom = False
      vaskerom()

    else:
      print("Ikke noe svar som heter", valg_roterom, ". Prøv på nytt.")


def trapp2():
  print("Du står nå i trapp 2")
  print("Foran deg er det 3 dører. En mørkeblå, en lyserød og en svart")
  asking_trapp2 = True
  while asking_trapp2 == True:
    valg_trapp2 = input("Hvilken dør velger du? ")

    if valg_trapp2 == "mørkeblå":
      asking_trapp2 = False
      soverom3()
    
    elif valg_trapp2 == "lyserød":
      asking_trapp2 = False
      kjøkken()
    
    elif valg_trapp2 == "svart":
      asking_trapp2 = False
      loft()

    else:
      print("Svaret", valg_trapp2, "er ikke gyldig. Prøv på nytt.")


def soverom3():
  print("Du står nå i soverom 3")
  print("Foran deg har du 2 dører, en mørkeblå, og en lyserosa.")
  asking_soverom3 = True
  while asking_soverom3 == True:
    valg_soverom3 = input("Hvilken dør vil du velge? ")
    
    if valg_soverom3 == "mørkeblå":
      asking_soverom3 = False
      trapp2()

    elif valg_soverom3 == "lyserosa":
      asking_soverom3 = False
      soverom2()

    else:
      print("Svaret", valg_soverom3, "er ikke gyldig. Prøv på nytt.")

  
def kjøkken():
  global liv, tau, armer, bein, spade, brødskive

  print("Du står nå på kjøkkenet.")

  
  if brødskive < 1:
    brødskive += 2
    print("Du fant 2 brødskiver på kjøkkenet.")
    print("Du har nå fått tak i mat, og kan forlate hytten. Prøv å finn utgangen")
  
  print("Foran deg er det 2 dører. En lyserød, og en neongul")
  asking_kjøkken = True
  while asking_kjøkken == True:
    valg_kjøkken = input("Hvilken dør velger du? lyserød eller neongul? ")

    if valg_kjøkken == "lyserød":
      asking_kjøkken = False
      trapp2()

    elif valg_kjøkken == "neongul":
      asking_kjøkken = False
      soverom2()
    
    else:
      print("Svaret er ugyldig. Vennligst prøv på nytt.")


def soverom2():
  print("Du står nå i soverom 2")
  print("Foran deg har du 4 dører.")
  print("En lyserosa, en neongul, en beige, og en fiolett")

  asking_soverom2 = True
  while asking_soverom2 == True:
    valg_soverom2 = input("Hvilken dør velger du? ")

    if valg_soverom2 == "lyserosa":
      asking_soverom2 = False
      soverom3()

    elif valg_soverom2 == "neongul":
      asking_soverom2 = False
      kjøkken()

    elif valg_soverom2 == "beige":
      asking_soverom2 = False
      utgang()

    elif valg_soverom2 == "fiolett":
      asking_soverom2 = False
      vaskerom()

    else:
      print("Svaret", valg_soverom2, "er ikke gyldig. Prøv igjen.")


def utgang():
  global liv, spade, tau, armer, bein, brødskive

  print("Du står nå ved utgangsdøren.")

  if brødskive >= 1:
    asking_utgang = True
    while asking_utgang == True:
     valg_utgang = input("Vil du gå ut av hytten? ")

     if valg_utgang == "ja":
      asking_utgang = False
      ute()
    
     elif valg_utgang == "nei":
      asking_utgang = False
      soverom2()

     else:
      print("Ingen svar som heter", valg_utgang, ". Prøv å skriv inn ja eller nei i stedet.")
  
  if brødskive < 1:
    print("Du kan ikke gå ut av hytten før du har funnet noe mat.")
    print("Fortsett å let")
    soverom2()
  

def ute():
  print("Du er nå ute av hytten.")
  print("Du fortsetter å gå, og ser en bilvei langt framme")
  print("Du følger bilveien, og kommer deg til slutt ut av skogen.")
  print("Gratulerer. Du fullførte spillet")
  print("(applaus)")
  startpånytt()

def startpånytt():
    asking_start = True
    while asking_start == True:
     valg = input("Vil du starte på nytt? ")

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