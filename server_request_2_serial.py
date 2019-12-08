import requests
import time
import serial
REQUEST_TEMPLATE = "http://localhost:1337/api/store?level={0:0.1f}" #ID for USB-C
#SERIAL_PATH = '/dev/tty.SLAB_USBtoUART' #ID for vanilla USB-A
SERIAL_PATH = '/dev/tty.usbserial-0001'
TANK_HEIGHT = 25.0
TANK_VOLUME = 10.0

def upload_level(level_per):
    url = REQUEST_TEMPLATE.format(level_per)
    print("Request sent: ", url)
    returned = requests.get(url)  
    print("Recieved: ", returned)       




def main():
    is_running = True
    
    s = serial.Serial(port=SERIAL_PATH, baudrate=57600, timeout=1)
     
    while is_running:
        s.flushInput()
        line = s.readline().strip()
        distance = line.decode('ascii')
        try:
            distance = float(distance)
            level_per = ((TANK_HEIGHT - distance)/TANK_HEIGHT)*100
            print("Successfully read distance: {0} equivalent to {1:0.1f}% full".format(distance, level_per))
            
            upload_level(level_per)            
              
        except:
            print("Recieved invalid level token: {}".format(distance))
            
            
            
        time.sleep(0.4)
   


main() #run program
