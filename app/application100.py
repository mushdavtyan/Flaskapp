#!/usr/bin/env python3

# ------------------------------------------------
# Program by Mushegh Davtyan
# Version      Date           Info
# 4.1          02-Jul-2020    Stable Version
# ----------------------------------------------
import time, socket
from flask import Flask

number = 100
application = Flask(__name__)
count = 0
hostname = socket.gethostname()


@application.route('/static')
# Response to integer values
def callsleep():
    global number
    global count
    sl = number * 0.001
    count += 1
    time.sleep(sl)
    return """host - {}, response-time- {} s,  current count - {}""".format(str(hostname), str(sl), str(count))
    


@application.route("/stats")
def index():
    global number
    global count
    sl = number * 0.001
    if sl >= 1:
        return 'hostname - {}, Total running counts with delay of  time {}s is  {}'.format(str(hostname), number, str(count))
    else:
        return 'hostname - {}, Total running counts with delay of time {}ms is  {}'.format(str(hostname), number, str(count))        

@application.route("/stats100")
def index100():
    global number
    global count
    sl = number * 0.001
    if sl >= 1:
        return 'hostname - {}, Total running counts with delay of  time {}s is  {}'.format(str(hostname), number, str(count))
    else:
        return 'hostname - {}, Total running counts with delay of time {}ms is  {}'.format(str(hostname), number, str(count))


#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
