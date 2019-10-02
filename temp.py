#coding: utf-8
import sys
from pyfiglet import Figlet
from time import sleep  
import Adafruit_DHT
import urllib2
import datetime

#constante
today = datetime.datetime.now()
sensor = Adafruit_DHT.DHT22
pin=4


def getSensorData():
    RH, T = Adafruit_DHT.read_retry(sensor, pin)

# return dict
    return (str("%.2f" % RH), str("%.2f" % T))
    
    
# main() function
def main():
    f = Figlet(font='slant')
    print f.renderText('DHT22 SENSOR \n\n')
    print today.strftime('Nous sommes le:  %d, %b %Y  %H:%M"')
    print '\n\n Starting SENSOR ...'

    baseURL = 'https://api.thingspeak.com/update?api_key=0CCT1NR5MO8K7Q1A'
   
    while True:
        try:
            RH, T = getSensorData()

            f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s" % (RH, T))

            #print f.read()
            print 'Humidité    ',RH,'\nTempérature ',T
            print '\n'           
            f.close()
            sleep(300)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
