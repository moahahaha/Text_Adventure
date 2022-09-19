from random import randint

liv = randint(3,10)
tau = 0
spade = 0
armer = 2
bein = 2


navn = input("Hei. Hva heter du?  ")
print("Velkommen", navn)
klar = input("Er du klar for å spille? ja eller nei?  ")
if klar == "nei":
    print("Nei vell")
    exit()

if klar == "ja":
    print("Du har" , liv, "liv")
    print("Det er en mørk og stormfull aften.")
print("Du befinner deg alene i en skog")
print("Plutselig får du øye på en boks")
print("Hva velger du å gjøre?")


valg = input("a: gå videre , b: åpne boksen ")



if valg == "b":
    print("Inni boksen er det en giftig slange")
    print("Hva gjør du?")
    slange = input("a: Løp i fra slangen , b: Stirr slangen inn i øynene ")

    if slange == "b":
        print("Du stirret slangen inn i øynene, og den angrep deg. Du mistet 3 liv")
        liv -= 3
    if liv < 1:
        print("Du gikk tom for liv, og døde")
        exit()
    if slange == "a":
        print("Du greide å løpe fra slangen")
    print("Du har", liv, "liv.") 

    print("Du fortsetter inn i skogen, og plutselig får du øye på en rød sopp")
    print("Hva velger du å gjøre", navn, "?")  

     
   
if valg == "a":
    print("Du gikk forbi boksen, og fortsetter inn i skogen.")
    spade += 1 
    print("Du fikk en spade")
    print("Du er veldig sulten, og plutselig får du øye på en rød sopp")
    print("hva gjør du?")


valg = input("a: spis soppen , b: gå videre ")

if valg == "a":
    print("Du spiste en giftig sopp, og mistet 2 liv")
    liv -= 2 
    if liv < 1:
        print("Du gikk tom for liv og døde")
        exit()
    print("Du har", liv, "liv igjen")
    print("Du fortsetter inn i skogen, og får øye på noen blå bær")
    print("Hva velger du å gjøre?")
    valg1 = input("a: spise bærene, b: gå forbi ")

    if valg1 =="a":
        print("Bærene var blåbær, og du fikk to liv")
        liv += 2
        print("Du har", liv, "liv igjen")
        print("Du fant også en spade")
        spade += 1

    if valg1 =="b":
        print("Du forbi dem, men ble veldig sulten, og mistet 3 liv")
        liv -= 3
        if liv < 1:
            print("Du gikk tom for liv og døde")
            print("Bedre lykke neste gang")
            exit()
        print("Du har", liv, "liv igjen")

if valg == "b":
    print("Du fortsetter inn i skogen, og fant en spade")
    spade += 1
    print("Du får øye på noen rosa bær.") 
    print("Hva velger du å gjøre?")
    valg2 = input("a: Gå forbi bærene, b: Spis bærene ")

    if valg2 == "a":
        print("Du gikk forbi bærene, og fant også et tau") 
        tau += 1
        
        

    if valg2 =="b":
        print("Bærene var veldig giftige, og du mistet 5 liv")
        liv -= 5
        if liv < 1:
            print("Du gikk tom for liv, og døde av de giftige bærene")
            print("Bedre lykke neste gang")
            exit()
        print("Du har", liv, "liv igjen")
    

print("Du har", tau, "tau,", spade, "spader og", liv, "liv")

print("Plutselig faller du ned i et dypt mørkt hull")



if tau >= 1:
    print("Vil du bruke tauet for å komme deg opp av hullet?")
    hull1 = input("ja, eller nei? ")
    if hull1 == "ja":
        print("Du klatret opp av hullet, og fortsetter inn i skogen")
    if hull1 == "nei":
        print("Du valgte å ikke klatre opp av hullet, og mistet 2 liv av sult")
        liv -= 2
        if liv < 1:
            print("Du døde av sult nede i hullet")
            exit()
        print("Så brukte du tauet til å klatre opp fra hullet likevell")
        tau -= 1
        print("Du har", liv, "liv,", tau, "tau og", spade, "spader.")

elif spade >= 1:
    print("Vil du bruke en spade å grave deg ut?")
    hull2 = input("ja eller nei? ")
    if hull2 == "ja":
        print("Du gravde deg ut av hullet")
    if hull2 == "nei":
        print("Du valgte å ikke grave deg ut, og mistet 2 liv pga. sult")
        liv -= 2
        if liv < 1:
            print("Du døde av sult nede i hullet")
            exit()
        print("Du brukte spaden til å grave deg ut likevell")
        spade -= 1
        print("Du har", liv, "liv,", spade, "spader og", tau, "tau")
    
else:
    print("Du hadde ingen tau eller spader til å komme deg opp av hullet med")
    print("Du døde nede i hullet")
    exit()
    

print("Etter å ha gått en stund kommer du til, møter du på en sint bjørn")
print("Hva gjør du?")


if tau >= 1:
    bjørn = input("a: løp, b: bruk tauet til å klatre opp i et tre, c: spill død")

    if bjørn == "a":
        print("Bjørnen var mye raskere enn deg, og tok deg igjen. Den anggrep og du mistet 3 liv")
        liv -= 3
        if liv < 1:
            print("Du mistet alle livene i bjørneangrepet og døde.")
            exit()
        print("Du har", liv, "liv.")

    if bjørn == "b":
        print("bjørnen klatret opp etter deg i treet, og angrep deg.")
        liv -= 3
        if liv < 1:
            print("Du mistet alle livene dine og døde")
            exit()
        print("Du mistet 3 liv")
        print("Du har", liv, "liv.")

    if bjørn == "c":
        print("Du valgte å spille død, og bjørnen gikk forbi deg.")
        print("Gratulerer, du har overlevd så langt, som er så langt jeg har kommet da.")

else:
    bjørn2 = input("a: løp, b: spill død, c: hopp på ryggen til bjørnen så den ikke ser deg.")

    if bjørn2 == "a":
        print("Bjørnen sprang etter deg, og spiste litt på deg")
        print("Du mistet en arm og 2 liv")
        liv -= 2
        armer -= 1
        if liv < 1:
            print("Bjørnen ombestemte seg, og spiste deg helt opp, og du døde")
            print("R.I.P")
            exit()
        print("Du har", liv, "liv og", armer, "armer")
    
    if bjørn2 == "b":
        print("Bjørnen syntes du så god ut, og den spiste på deg når du spilte død")
        print("Du mistet 2 liv og et bein")
        liv -= 2
        bein -= 1
        if liv < 1:
            print("Bjørnen spiste deg helt opp, og du døde.")
            exit()
        print("Du har", liv, "liv og", bein, "bein, og må nå dessverre hinke rundt")

    if bjørn2 == "c":
        print("Bjørnen ble redd, og sprang rundt, og du datt av i en myk busk") 
        print("Gratulerer, du har overlevd så langt, som er så langt jeg har kommet da.")