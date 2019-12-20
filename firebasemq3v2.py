# This solution needs to be reworked - number of samples that will be taken depend on CPU speed
import time
import sys
from mq3 import *
import statistics
from datetime import datetime
# from firebase import firebase

MEASURING_TIME          = 5000           # in miliseconds
PERC_MIN_VAL            = 0.05
PERC_MAX_VAL            = 10.0
SEND_TO_FIREBASE        = True

def measure():
    mq = MQ();
    samples = []
    time_start = int(datetime.timestamp(datetime.now()) * 1000)

    while int(datetime.timestamp(datetime.now()) * 1000) - time_start < MEASURING_TIME:
        try:
            perc = mq.MQPercentage()
        except Exception as e:
            print(e)
        else:
            if PERC_MIN_VAL < perc["GAS_ALC"] < PERC_MAX_VAL:
                print("\r")
                print("\033[K")
                print("Alcohol Detection Level: %g mg/L" % (perc["GAS_ALC"]))
                print("Promiles: %g" % (2.1 * perc["GAS_ALC"]))
                samples.append(perc["GAS_ALC"])
    return samples

def main():
    value = statistics.median(measure())
    print("Finished measuring. Final value: ", value)

    if SEND_TO_FIREBASE:
        print("Sending to Firebase...")
        # firebase = firebase.FirebaseApplication('https://drunkornot-2fb5d.firebaseio.com/')
        # read_MQ3 = {"ethanol": value}
        # firebase.post('/MQ3/', read_MQ3)

if __name__ == "__main__":
    main()