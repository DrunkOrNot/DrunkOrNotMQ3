import time
import sys
from mq3 import *
#from firebase import firebase

mq = MQ();

while True:
        time.sleep(0.1)
        try:
                perc = mq.MQPercentage()
        except Exception as e :
                #sys.stdout.write(e)
                sys.stdout.flush()
        else:                          
                #if  0.05 < perc["GAS_ALC"] < 10.0:               
                        sys.stdout.write("\r")
                        sys.stdout.write("\033[K")
                        #sys.stdout.write("Alcohol Detection Level: %g mg/L" % (perc["GAS_ALC"]))
                        sys.stdout.write("Promiles: %g" % (2.1 * perc["GAS_ALC"]))
                        sys.stdout.flush()

        
        #firebase = firebase.FirebaseApplication('https://drunkornot-2fb5d.firebaseio.com/')
        #read_MQ3 = {"ethanol": perc}
        #firebase.post('/MQ3/', read_MQ3)

def calculate(percentage):
        return 2.1 * percentage
        
