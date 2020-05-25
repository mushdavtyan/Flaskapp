#!/usr/bin/env python3

# ------------------------------------------------
# Program by Mushegh Davtyan
# Version      Date           Info
# 3.5          21-May-2020    Stable Version
# ----------------------------------------------
import time, socket
from flask import Flask



application = Flask(__name__)
count = 0
hostname = socket.gethostname()



@application.route('/<int:number>')
# Response to integer values
def callsleep(number):
    sl = number * 0.001
    global count
    count += 1
    time.sleep(sl)
    if sl >= 1:
        return """host - {}, response-time- {} s,  current count - {}""".format(str(hostname), str(sl), str(count))
    else:
        return """host - {}, response-time- {} ms,  current count - {}""".format(str(hostname), str(sl), str(count))


@application.route("/statistics")
def index():
    return 'hostname - {}, Total running counts  is  {}'.format(str(hostname),  str(count))
   


#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
