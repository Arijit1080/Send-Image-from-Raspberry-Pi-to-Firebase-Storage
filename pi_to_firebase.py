import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase

firebaseConfig = {
    'apiKey': "XXXXX",
    'authDomain': "XXXXX",
    'databaseURL': "XXXXX",
    'projectId': "XXXXX",
    'storageBucket': "XXXXX",
    'messagingSenderId': "XXXXX",
    'appId': "XXXXX",
    'measurementId': "XXXXX"

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

camera = PiCamera()

while True: 
  try:
    if GPIO.input(10) == GPIO.HIGH:
        print("pushed")
        now = datetime.now()
        dt = now.strftime("%d%m%Y%H:%M:%S")
        name = dt+".jpg"
        camera.capture(name)
        print(name+" saved")
        storage.child(name).put(name)
        print("Image sent")
        os.remove(name)
        print("File Removed")
        sleep(2)
	
	
  except:
        camera.close()

