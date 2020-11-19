# from __future__ import division                  #helpt bij het jet importen zorgt voor geen verwaring

import RPi.GPIO as GPIO  # Import library GPIO
import time  # Import library Time.
import Adafruit_PCA9685  # Import library van PCA9685 module.
from random import randint
import datetime

from flask import Blueprint, render_template, redirect, url_for, session, request, g

now = datetime.datetime.now()

Game = Blueprint("Game", __name__, static_folder="static", template_folder="templates")

GPIO.setmode(GPIO.BCM)  # Aangeven welke type pin notering er gebruikt word
GPIO.setwarnings(False)  # Zet waarschuwing uit

# afstandsensor
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)  # Set pin als GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin als GPIO in

game_active = 0

def afstand_meting():
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    time.sleep(2)

    GPIO.output(TRIG, True)  # Verstuur een signaal(true)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)  # Zet trigger na 0,01ms naar 0(low)

    while GPIO.input(ECHO) == 0:  # Check als  de ECHO LOW (0) is
        pulse_start = time.time()  # Bewaar de genoteerde tijd van de low pulse

    while GPIO.input(ECHO) == 1:  # Check als  de ECHO HIGH (1) is
        pulse_end = time.time()  # Bewaar de laatst genoteerde tijd van de low pulse

    pulse_lengte = pulse_end - pulse_start  # bereken de pulse looptijd

    distance = (pulse_lengte * 24300) / 2  # vermenigvuldig met de sonische snelheid (34300 cm/s :2 ) omdat heen en weer
    distance = round(distance, 2)
    distance = int(distance)
    return distance


def game():
    pwm = Adafruit_PCA9685.PCA9685()  # Initialiseer de PCA9685 met het standaardadres (basis adddres 0x40).
    pwm.set_pwm_freq(50)  # Verander de PWM frequentrie naar 50MHZ

    #puten
    geraakt = 0
    punten_nomering = 0

    # decaleer ik waarden
    sensor1 = 4
    sensor2 = 5
    sensor3 = 27
    sensor4 = 22
    sensor5 = 17

    # pinnen instellen
    GPIO.setup(sensor1, GPIO.IN)
    GPIO.setup(sensor2, GPIO.IN)
    GPIO.setup(sensor3, GPIO.IN)
    GPIO.setup(sensor4, GPIO.IN)
    GPIO.setup(sensor5, GPIO.IN)

    # Hier congigureer ik de minimaale en maximaale waardes voor de pulse
    servo_actief = 100  # Min pulse length out of 4096
    servo_rust = 350  # Max pulse length out of 4096 (90 graden)
    servo1 = 11
    servo2 = 12
    servo3 = 0
    servo4 = 1
    servo5 = 7

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)
    pwm.set_pwm(servo4, 0, servo_rust)
    pwm.set_pwm(servo5, 0, servo_rust)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_actief)
    pwm.set_pwm(servo2, 0, servo_actief)
    pwm.set_pwm(servo3, 0, servo_actief)
    pwm.set_pwm(servo4, 0, servo_actief)
    pwm.set_pwm(servo5, 0, servo_actief)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)
    pwm.set_pwm(servo4, 0, servo_rust)
    pwm.set_pwm(servo5, 0, servo_rust)

    tijd_limiet = 30  # aantal seconde dat er gespeeld kan worden
    start_tijd = time.time()  # start tijd is de actueele tijd van nu
    pervRandomTarget = -1
    while True:  # loop altijd
        gespeeld_tijd = time.time() - start_tijd  # berekening gespeelde tijd

        if gespeeld_tijd >= tijd_limiet:  # als gespeelde tijd groter is dan tijd limiet stop de loop
            break

        while True:
            RandomTarget = randint(0, 4)
            if RandomTarget != pervRandomTarget:
                break

        pervRandomTarget = RandomTarget

        if RandomTarget == 0:
            pwm.set_pwm(servo1, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor1):
                    pwm.set_pwm(servo1, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 1:
            pwm.set_pwm(servo2, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor2):
                    pwm.set_pwm(servo2, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 2:
            pwm.set_pwm(servo3, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor3):
                    pwm.set_pwm(servo3, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 3:
            pwm.set_pwm(servo4, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor4):
                    pwm.set_pwm(servo4, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

        if RandomTarget == 4:
            pwm.set_pwm(servo5, 0, servo_actief)
            time.sleep(0.5)
            while True:
                if GPIO.input(sensor5):
                    pwm.set_pwm(servo5, 0, servo_rust)
                    geraakt += 1
                    break

                gespeeld_tijd = time.time() - start_tijd

                if gespeeld_tijd > tijd_limiet:
                    break

    pwm.set_pwm(servo1, 0, servo_actief)
    pwm.set_pwm(servo2, 0, servo_actief)
    pwm.set_pwm(servo3, 0, servo_actief)
    pwm.set_pwm(servo4, 0, servo_actief)
    pwm.set_pwm(servo5, 0, servo_actief)

    time.sleep(1)

    pwm.set_pwm(servo1, 0, servo_rust)
    pwm.set_pwm(servo2, 0, servo_rust)
    pwm.set_pwm(servo3, 0, servo_rust)
    pwm.set_pwm(servo4, 0, servo_rust)
    pwm.set_pwm(servo5, 0, servo_rust)

    afstand = afstand_meting()

    if afstand <= 10:
        punten_nomering = 0

    elif afstand >= 10 & afstand <= 30:
        punten_nomering = 1

    elif afstand >= 30 & afstand < 50:
        punten_nomering = 2

    elif afstand >= 50 & afstand <= 100:
        punten_nomering = 3

    elif afstand >= 100:
        punten_nomering = 4

    totaalscore = geraakt * punten_nomering
    gemiddelde_tijd = totaalscore/tijd_limiet

    file = open("../Website/highscore.txt", "a")
    file.write("\n")
    file.write(g.user.username + " " + str(totaalscore) + " " + str(geraakt) + " " + str(afstand) + " " +
        str(punten_nomering) + " " + str(gemiddelde_tijd) + " " + now.strftime("%Y-%m-%d %H:%M"))
    file.close()

@Game.route("/", methods=['GET', 'POST'])
def game_site_nl(game_active=game_active):
    startup = 1
    while True:
        if startup == 1:
            if game_active == 0:
                game_active = 1
                game()
                game_active = 0
                return redirect(url_for('Nederlands.homepage_nl'))
            else:
                return redirect(url_for('Nederlands.homepage_nl'))
        startup = 0

        return render_template("Space_Shooters_Web_game.html")
