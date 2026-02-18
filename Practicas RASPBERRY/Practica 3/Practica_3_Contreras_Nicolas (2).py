import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import os
import time
import random

PIR = 17
LED_AMARILLO = 27
LED_ROJO = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED_AMARILLO, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)

print("sistema de alarma activado")

contrasenas = {'color':'azul','flor':'amapola','animal':'perro','ciudad':'madrid','colegio':'salesianos'}

claves = list(contrasenas.keys())

while True:
    GPIO.output(LED_AMARILLO,False)
    GPIO.output(LED_ROJO,False)
    
    if GPIO.input(PIR) == 1:
        print("Movimiento detectado")

        GPIO.output(LED_AMARILLO, True)

        num = random.randint(0,4)
        clave = claves[num]

        respuesta = input("Dime un " + clave + ": ")

        if respuesta == contrasenas[clave]:
            print("Correcto")
            GPIO.output(LED_AMARILLO, False)
            GPIO.output(LED_ROJO, False)
        else:
            print("Incorrecto")
            GPIO.output(LED_ROJO, True)
            GPIO.output(LED_AMARILLO,False)
            print("antes")
            os.system('cp plantilla.call llamda.call')
            os.system('mv llamada.call /var/spool/asterisk/outoging/')
            print('despues')
    else:
        print("no hay movimiento")

    time.sleep(2)