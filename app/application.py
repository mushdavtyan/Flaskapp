#!/usr/bin/env python3

# ------------------------------------------------
# Program by Mushegh Davtyan
# Version      Date           Info
# 2.0          18-Apr-2020    Initial Version
# ----------------------------------------------
import time, socket
from flask import Flask



application = Flask(__name__)
count = 0
hostname = socket.gethostname()


@application.route('/<int:number>')
# Response to integer values
def callsleep(number):
    global count
    count += 1
    time.sleep(int(number) / 1000)
    return """<font color="green"><H1  ALIGN="Center">Kubernetes Load-Balancer check page</H1>
              <font color="green"><H4  ALIGN="Center">Call with sleeping time {} millisec. Running  count <H1  ALIGN="Center">{}</H1></H4>""".format(number, str(count))


@application.route("/stats")
def index():
    return '{} {}'.format(str(hostname), str(count))


#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------