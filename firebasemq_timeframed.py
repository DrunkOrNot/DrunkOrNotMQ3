import time
import sys
from mq3 import *
import statistics
from datetime import datetime
from firebase import firebase

MEASURING_TIME          = 5000           # in miliseconds
NUM_SAMPLES             = 1000
PERC_MIN_VAL            = 0.05
PERC_MAX_VAL            = 10.0
firebase = firebase.FirebaseApplication('https://drunkornot-2fb5d.firebaseio.com/')

def measure():
    mq = MQ();
    samples = []
    frame_duration = MEASURING_TIME / NUM_SAMPLES
    time_start = int(datetime.timestamp(datetime.now()) * 1000)
    frame_start = time_start

    while int(datetime.timestamp(datetime.now()) * 1000) - time_start < MEASURING_TIME:
        if (datetime.timestamp(datetime.now()) * 1000) - frame_start >= frame_duration:
            frame_start = int(datetime.timestamp(datetime.now()) * 1000)
            try:
                perc = mq.MQPercentage()
            except Exception as e:
                print(e)
            else:
                print("\r")
                print("\033[K")
                print("Alcohol Detection Level: %g mg/L" % (perc["GAS_ALC"]))
                print("Promiles: %g" % (2.1 * perc["GAS_ALC"]))
                if PERC_MIN_VAL < perc["GAS_ALC"] < PERC_MAX_VAL:
                    samples.append(perc["GAS_ALC"])
    print("Samples taken: ", len(samples))
    return samples

def main():
    samples = measure()
    if len(samples) != 0 :
        value = statistics.median()
        print("Finished measuring. Final value: ", value)
    else :
        value = 0;

    localtime = time.asctime(time.localtime(time.time())) 
    print("Sending to Firebase...")
    read_MQ3 = {"ethanol": value}
    firebase.post('/MQ3/', read_MQ3)

if __name__ == "__main__":
    main()
        
