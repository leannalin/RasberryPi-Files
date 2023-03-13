# Import GPIO library, modules for time, access to sensor, flask app
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_veml6075
from time import sleep 
from flask import Flask, render_template
app = Flask(__name__)

# Init 
in1 = 11
in2 = 12
in3 = 15
in4 = 16
en1 = 17 
en2 = 18 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(in1, GPIO.OUT) 
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
print('Motor starting')

# Setting up I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

# Sensor collecting data 
def main():
        print("uv sensor test start")
while True:
    uv = veml.uv_index
    veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)
    print("UV index:", veml.uv_index)
    time.sleep(1)
    
# setting up Flask app to display the data of sensor  
@app.route('/')
def index():
    while True:
    print("UV index:", veml.uv_index)
    time.sleep(1) 
    return render_template('index.html',uv=uv )

#test using 'python3 ~/uvsensor.py'  
    
# Starting the motor and setting if statement for when oil is detected, motors turn off and dispersent is activated 
if veml.uv_index > 5
        while True: 
            print("boat starting")
            print("forward")

            try:

                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                time.sleep(5)

        print("turning")

                 GPIO.output(in1,GPIO.HIGH)
                 GPIO.output(in2,GPIO.LOW)
                 GPIO.output(in3,GPIO.LOW)
                 GPIO.output(in4,GPIO.HIGH)
                 time.sleep(2)

         print("forward")   

                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                time.sleep(5)

         print("turning")

                 GPIO.output(in1,GPIO.HIGH)
                 GPIO.output(in2,GPIO.LOW)
                 GPIO.output(in3,GPIO.LOW)
                 GPIO.output(in4,GPIO.HIGH)
                 time.sleep(2)

                 except(KeyboardInterrupt):
            # If keyboard interrupt is detected then it exits cleanly!
            print('Done!')
                GPIO.output(in1, False)
                GPIO.output(in2, False)
                GPIO.output(in3, False)
                GPIO.output(in3, False)
                quit()

else: 
        print('stopping')
        
                 GPIO.output(in1,GPIO.LOW)
                 GPIO.output(in2,GPIO.LOW)
                 GPIO.output(in3,GPIO.LOW)
                 GPIO.output(in4,GPIO.LOW)
                 time.sleep(5)
                
                print('dispersing')
                
                 GPIO.output(en1,GPIO.HIGH)
                 GPIO.output(en2,GPIO.LOW)
                
        
            
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
