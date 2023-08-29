from gpiozero import Button
from signal import pause
from create import IFTTT_notification

newNotification = IFTTT_notification()

def say_hello() :
    newNotification.Send_mail()


# def Send_mail() :
#     print(newNotification)
     


button = Button(2)

button.when_pressed = say_hello
pause()