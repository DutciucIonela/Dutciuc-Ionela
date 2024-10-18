import string
#Textul articoluluii copiat de pe internet
text="""[Deputatul AUR care a primit fraudulos locuință de la MApN și a vândut-o de 13 ori mai scump. ]"""
#Imparte sirul in doua parti egale
lungime=len(text)
mijloc=(lungime+1)//2 #Am adaugat +1 pentru a trata cazul de imparitate
prima_parte=text[:mijloc]
a_doua_parte=text[mijloc:]
#Prima parte care transforma literele in majuscule si elimina spatiile goale
prima_parte=prima_parte.upper().strip()
#A doua parte care inverseaza ordinea caracterelor , transforma prima litera in majuscula si elimina caracterele de punctuatie
a_doua_parte=a_doua_parte[::-1].capitalize()
#Combinarea celor doua parti
rezultat=prima_parte+a_doua_parte
#Afisarea rezultatului
print(rezultat)