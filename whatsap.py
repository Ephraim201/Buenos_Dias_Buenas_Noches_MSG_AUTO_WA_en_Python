import pywhatkit
import datetime
import time
from frases import *
import random

hora_actual = datetime.datetime.now().time()
print("La hora actual es:", hora_actual.strftime("%H:%M:%S"))
numero = "+?? #########" # <- numero de whatsap de la persona a la que le envies los mensajes 
frase_aleatoria_dia = random.choice(frases_de_buenos_dias)
frases_aleatorias_tardes = random.choice(frases_de_buenas_tardes)
frases_aleatorias_noches = random.choice(frases_de_buenas_noches)

hora_inicio_mañana = datetime.time(8, 00) 
hora_fin_mañana = datetime.time(8, 30)  

hora_inicio_tarde= datetime.time(13, 00) 
hora_fin_tarde = datetime.time(13, 30)  

hora_inicio_noche = datetime.time(22, 00) 
hora_fin_noche = datetime.time(22, 30)  


repetir = int(0)


while True:

    hora_actual = datetime.datetime.now().time()
    
    # Comprobar si la hora actual está dentro del rango
    if hora_inicio_mañana <= hora_actual <= hora_fin_mañana and repetir != 1:
        print("El mensaje a sido enviado")
        pywhatkit.sendwhatmsg_instantly(numero,frase_aleatoria_dia,tab_close = False)
        repetir= int(1)
    
    if hora_inicio_tarde <= hora_actual <= hora_fin_tarde and repetir != 2:
        print("El mensaje a sido enviado")
        pywhatkit.sendwhatmsg_instantly(numero,frases_aleatorias_tardes,tab_close = False)
        repetir= int(2)
    
    if hora_inicio_noche <= hora_actual <= hora_fin_noche and repetir != 3:
        print("El mensaje a sido enviado")
        pywhatkit.sendwhatmsg_instantly(numero,frases_aleatorias_noches,tab_close = False)
        repetir= int(3)
    
    time.sleep(60) 

