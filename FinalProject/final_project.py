from gpiozero import MCP3008
import time
import ADC0832
import os

def init():
    ADC0832.setup()
    
def soilMoisture():
    res = ADC0832.getADC(0)
    vol = 3.3/255 * res
    moisture_percentage = (vol / 3.3) * 100
    time.sleep(0.2)
    print ('voltage: %.2fV' %(vol))
    print(f'Moisture: {moisture_percentage:.2f}%')
    return "{:.2f}".format(vol)
    

def loop():
    while True:
        soilMoisture()

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        print ('The end !')