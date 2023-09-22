#d)
#Skriv en funksjon som tar inn ei liste med flyttall og en enkeltverdi. 
#Funksjonen skal telle antall elementer i lista som er større enn eller 
#lik den oppgitte verdien og returnere dette.



minliste=[1.3, 1.7, 2.9,84.2,56.4,99.67,5,34.3]

verdi = 4.55


def listefun(minliste,verdi):
    
    antall=0
    
    for element in minliste:
        
        
        if element >=verdi:
            antall+=1
        
    return antall


antall_elementer = listefun(minliste, verdi)
print(antall_elementer)
            
            
    
    