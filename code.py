# Import GPIO library, modules for time, access to sensor, flask app
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_ltr390
from time import sleep 
from flask import Flask, render_template
app = Flask(__name__)

# Init 
en1 = 12 
en2 = 13 
in1 = 17
in2 = 18
in3 = 22
in4 = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(in1, GPIO.OUT) 
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
print('Motor starting')

# Setting up I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

ltr = adafruit_ltr390.LTR390(i2c)

# Sensor collecting data 
def main():
  print("uv sensor test start")
  while True:
    print("UV index:", ltr.uvs)
    time.sleep(0.5)
    
# setting up Flask app to display the data of sensor  
@app.route('/')
def index():
  while True: 
    print("UV index:", ltr.uvs)
    time.sleep(0.5)
    return render_template('index.html', ltr.uvs)

#test using 'python3 ~/uvsensor.py'  
    
# Starting the motor and setting if statement for when oil is detected, motors turn off and dispersent is activated 

count = 0
def moving(count,en1,en2,in1,in2,in3,in4):
  while count < 3: 
    if ltr.uvs < 5:
      count = count+1
    if ltr.uvs >= 5:
      print("boat starting")
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
        
      count = 0
        #Sets the count back to 0 so that it will count values less than 5 unconsecutively
  return(count)

def whenlessthan5(count, in1, in2, in3, in4):
  if count == 3:
    print("stopping")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(5)
  
    print("dispersing")
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.LOW)
    
    count = 0
    count = moving()


#main program
index()
main()

try:
  count = moving(count,en1,en2,in1,in2,in3,in4) #calling subroutine for the first time to start the loop
  whenlessthan5(count, in1, in2, in3, in4)
                
#Triggering motor for dispersant       
except:
        # If keyboard interrupt is detected then it exits cleanly!
  print("Done!")
  GPIO.output(in1, False)
  GPIO.output(in2, False)
  GPIO.output(in3, False)
  GPIO.output(in3, False)
  quit()
