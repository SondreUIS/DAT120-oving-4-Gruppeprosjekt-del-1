#Fila «lister_for_del_1.py» er delt ut sammen med denne øvingen. Bruk funksjonen fra
#oppgave d) på lista «temperaturer» fra denne fila. Anta at hvert innslag er
#maksimaltemperaturen for en dag. Finn antall sommerdager (over 20), høysommerdager
#(over 25) og tropedager (over 30).


minliste=[-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]


verdi_sommerdag=20
verdi_høysommer=25
verdi_tropedag = 30
def listefun_3(minliste,verdi_tropedag):
    
    antall_3=0
    
    for element in minliste:
        
        
        if element >30:
            antall_3+=1
        
    return antall_3

def listefun_2(minliste,verdi_høysommer):
    
    antall_2=0
    
    for element in minliste:
        
        
        if element in range(verdi_høysommer,30) :
            antall_2+=1
        
    return antall_2

def listefun(minliste,verdi_sommerdag):
    
    antall_1=0
    
    for element in minliste:
        
        
        if element in range(verdi_sommerdag,25) :
            antall_1+=1
        
    return antall_1


sommerdager=listefun(minliste, verdi_sommerdag)
høysommerdager=listefun_2(minliste, verdi_høysommer)
tropedager = listefun_3(minliste, verdi_tropedag)
print(f'Det er {sommerdager} sommerdager, {høysommerdager} høysommerdager og {tropedager} tropedager')
            
