import json
import datetime
from collections import Counter
import json
import datetime
import sys


out = {"books": [], "cds": [], "films": []}

everything = {"library": {}}

helabiblan = "my_library_register.json" 
   
def get_inputs_book():
    #user input to record the log
    
    dbok =  {}
    print("******************Böcker************************")
    dbok['BookTitel'] = input("Lägg in en bok titel: ")
    dbok['Bookforfattare'] = input("Vad heter forfattaren: ")
    dbok['BookAntal'] = input("Hur många sidor har boken: ")
    dbok['BookInkopspris'] = input("Vad var EttInkopspris: ")
    dbok['BookInkopesar'] = input("Vad var EttInkopesar: ")
    
    out['books'].append(dbok)
    
    return out

def get_inputs_cd():
    #user input to record the log
    
    dcd =  {}
    print("******************CD************************")
    dcd['CdTitel'] = input("Lägg in en cd titel: ")
    dcd['CdArtist'] = input("Vad heter artisten: ")
    dcd['CdAntalspar'] = input("Hur många spår finns det: ")
    dcd['CdLangd'] = input("Vad är längden: ")
    dcd['CdInkopspris'] = input("Vad var inköpspriset: ")

    out['cds'].append(dcd)
    
    return out

def get_inputs_film():
    #user input to record the log

    dfilm =  {}
    print("******************FILM************************")
    dfilm['FilmTitel'] = input("Lägg in en film titel: ")
    dfilm['FilmRegissor'] = input("Vad heter artisten: ")
    dfilm['FilmLangd'] = input("Hur lång är filmen: ")
    dfilm['FilmInkopspris'] = input("Vad var FilmInkopspris: ")
    dfilm['FilmInkopesar'] = input("Vad var inköpsåret: ")
    dfilm['Forslitningsgrad'] = input("Ange forslitningsgrad mellan 1-10 : ")
    
    
    out['films'].append(dfilm)
    
    return out    


def visaplus():
    
    savetest()
    
    Final_Lista = makealista() 
    skrivut_hela_biblioteket(Final_Lista)
    
    

def menufinal():        
    
    while True:
        a = input("""
                     Chose the details you like to register  
                     A: Registera böcker
                     B: Registera cdskivor
                     C: Registera filmer
                     D: VISA LIBRARY
                     Q: Quit
                     Please enter your val: """).lower()
        if a=="a":
            get_inputs_book()
        elif a=="b":
            get_inputs_cd()           
        elif a=="c":
            get_inputs_film()
        elif a=="d":
            visaplus()                      
        elif a=="q":
            savetest()
            break        
        else:
            print("Välj ett alternative")        
        



def savetest():
    
    everything["library"].update(out)
    
    with open(helabiblan,'w') as f:
        json.dump(everything, f, indent=2)
        
    
        

#--------------------------book----------------------
def rakna_bok(År, price):
    ÅretNu = datetime.datetime.now()
    age = ÅretNu.year - År
    if age > 50:
        price = price*(0.9**50)*(1.08**(age-50))
        return round(price, 2)
    else:
        price = price*(0.9**age)
        return round(price, 2)



#---------------------------film-----------------------------------

def taborttioprocent(År, price):  
    ÅretNu = datetime.datetime.now()
    age = ÅretNu.year - År
    price = price*(0.9**age)
    return round(price, 2) 





def the_film_worth(FilmInkopspris, förslitningsgrad ):
    # // annvänd om dom råka trycka enter
    if förslitningsgrad == 1:
        tioprocent = FilmInkopspris  * 0.10
        tioNya = tioprocent + FilmInkopspris 
        return round(tioNya)
    elif förslitningsgrad == 2:
        tjugoprocent = FilmInkopspris  * 0.20
        tjugoNya = tjugoprocent + FilmInkopspris
        return round(tjugoNya) 
    elif förslitningsgrad == 3:
        trettioprocent = FilmInkopspris  * 0.30
        trettioNya = trettioprocent + FilmInkopspris 
        return round(trettioNya)
    elif förslitningsgrad == 4:
        fyrtioprocent = FilmInkopspris  * 0.40
        fyrtioNya = fyrtioprocent + FilmInkopspris 
        return round(fyrtioNya)
    elif förslitningsgrad == 5:
        femtioprocent = FilmInkopspris  * 0.50
        femtioNya = femtioprocent + FilmInkopspris 
        return round(femtioNya) 
    elif förslitningsgrad == 6:
        sextioprocent = FilmInkopspris  * 0.60
        sextio = sextioprocent + FilmInkopspris 
        return round(sextio)
    elif förslitningsgrad == 7:
        sjutioprocent  = FilmInkopspris  * 0.70
        sjutioNya = sjutioprocent + FilmInkopspris 
        return round(sjutioNya)
    elif förslitningsgrad == 8:
        åttioprocent = FilmInkopspris  * 0.80
        åttioNya = åttioprocent + FilmInkopspris 
        return round(åttioNya)
    elif förslitningsgrad == 9:
        nittoprocent = FilmInkopspris  * 0.90
        nittioNya = nittoprocent + FilmInkopspris
        return round(nittioNya) 
    elif förslitningsgrad == 10:
        hundraprocent = FilmInkopspris
        return round(hundraprocent) 




#---------------------------cd-----------------------------------


def taborttioprocent(År, price):  
    ÅretNu = datetime.datetime.now()
    age = ÅretNu.year - År
    price = price*(0.9**age)
    # print("s4", price) 
    return round(price, 2) 

def finalworth(Titel, Artist, Thelist, FirstPris):
    TitelPlusArtist = Titel + " " + Artist
    Sametitels = Thelist.count(TitelPlusArtist)
    # print(Sametitels)
    Worth = FirstPris / Sametitels
    return round(Worth)



def makealista():
    with open(helabiblan, 'r') as f:
        info = json.load(f)     
        access_library = info['library']
        lista1 = []
        lista2 = []
        lista = []
        # här vill jag nå sakerna under results som komver vara titel och artist
        for cd_data in access_library['cds']:
            titel_cd = cd_data['CdTitel']
            artist_cd = cd_data['CdArtist']
            lista1.append(titel_cd)
            lista2.append(artist_cd)
        for name, surname in zip(lista1, lista2):
            lista.append(name + " " + surname)
    return lista             
            
        
#-----------------------------------------


def skrivut_hela_biblioteket(lista):    

    with open(helabiblan, 'r') as f:
         
        info = json.load(f)
        
    access_library = info['library']
    
    books = access_library['books']
    cds = access_library['cds']
    films = access_library['films']
    
    
    sorted_list_books = sorted(books, key=lambda k: (k['BookTitel']))
    sorted_list_cds = sorted(cds, key=lambda k: (k['CdTitel']))
    sorted_list_films = sorted(films, key=lambda k: (k['FilmTitel']))
    
    for book_data in sorted_list_books:

        BookTitel = book_data['BookTitel']
        Bookforfattare = book_data['Bookforfattare']
        BookAntal = book_data['BookAntal']
        BookInkopspris = int(book_data['BookInkopspris'])
        BookInkopesar = int(book_data['BookInkopesar'])
        VardetNu = (rakna_bok(BookInkopesar, BookInkopspris))
        print("-------------------------------------------------------------sorterad----------------------------------------------------------------")
        print("BookTitel", BookTitel , "forfattare",Bookforfattare, "Antalsidor", BookAntal, "Inkopspris", BookInkopspris, "Inkopesar", BookInkopesar, "NyaVärdet:", VardetNu, "kr")    

    for cd_data in sorted_list_cds:

        CdTitel = cd_data['CdTitel']
        CdArtist = cd_data['CdArtist']

        CdAntalspar = cd_data['CdAntalspar']
        CdLangd = int(cd_data['CdLangd'])
        CdInkopspris = int(cd_data['CdInkopspris'])

        nyttpris = finalworth(CdTitel, CdArtist, lista, CdInkopspris)
     
        print("-------------------------------------------------------------sorterad----------------------------------------------------------------")
        print("CdTitel:", CdTitel , "Artist:", CdArtist, "EttAntalspar:",CdAntalspar, "EnLangd:", CdLangd, "EttInkopspris:", CdInkopspris, "NyaVärdet:", nyttpris, "kr")    

    for film_data in sorted_list_films:

        FilmTitel = film_data['FilmTitel']
        FilmRegissor = film_data['FilmRegissor']
        FilmLangd = int(film_data['FilmLangd'])
        FilmInkopspris = int(film_data['FilmInkopspris'])
        FilmInkopesar = int(film_data['FilmInkopesar'])
        Forslitningsgrad = int(film_data['Forslitningsgrad'])

        MinusTio = taborttioprocent(FilmInkopesar, FilmInkopspris)
        filmpris = the_film_worth(MinusTio, Forslitningsgrad)

        print("-------------------------------------------------------------sorterad-----------------------------------------------------------------")
        print("FilmTitel:", FilmTitel , "Regissor:", FilmRegissor, "EnfilmLangd:",FilmLangd , "min", "FilmInkopspris:", FilmInkopspris, "kr", "EttInkopesar:", FilmInkopesar, "NyaVärdet:", filmpris, "kr")

 
menufinal()
 
 
 




