RasberryPi-Files
The python script for an oil detecting boat for our PAPi competition

# Setting up 
Enter this command into the terminal to set up I2C 
```
sudo raspi-config
```
Then follow this [tutorial](https://www.mathworks.com/help/supportpkg/raspberrypiio/ref/enablei2c.html) to enable the I2C connection 

Run this command in the terminal to install the UV sensor
```
sudo pip3 install adafruit-circuitpython-ltr390
```
Run this command in the terminal to install the Flask app
```
sudo apt install python3-flask 
```

