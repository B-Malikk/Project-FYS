import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.IN)

servo1=GPIO.PWM(11,50)#pin 11 heeft 50 herts
SensorGPIO = 7
servo1.start(1.5)#draait direct 90 garden


while True:
    if GPIO.input(SensorGPIO):  #als input komt vanuit pin doe dit
        servo1.ChangeDutyCycle(6)  # brengt terug naar start plek
        time.sleep(3)#omdat het even duurt tot dat de pulse de servomotor heeft bereikt (anders gaat het direct naar break)
        break



#servo1.stop()
print("Test succesvol!!!!!!!!")

#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#pwm.ChangeDutyCycle(5)
#


