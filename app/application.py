#!/usr/bin/env python3

# ------------------------------------------------
# Program by Mushegh Davtyan
#
#
# Version      Date           Info
# 1.0          18-Apr-2020    Initial Version
#
# ----------------------------------------------
import time
from flask import Flask, render_template

application = Flask(__name__)
count_1 = count_5 = count_10 = count_15 = count_20 = 0


@application.route('/<int:number>')
# Response to integer values
def callsleep(number, color='black', retcount='Not supported. Please type 1, 5, 10, 15, 20 values'):
    if number == 1:
        global count_1
        count_1 += 1
        retcount = count_1
        color = 'green'
    elif number == 5:
        global count_5
        count_5 += 1
        retcount = count_5
        color = 'yellow'
    elif number == 10:
        global count_10
        count_10 += 1
        retcount = count_10
        color = 'blue'
    elif number == 15:
        global count_15
        count_15 += 1
        retcount = count_15
        color = 'blue'
    elif number == 20:
        global count_20
        count_20 += 1
        retcount = count_20
        color = 'orange'
    time.sleep(int(number))
    return """<font color="{}"><H1  ALIGN="Center">Kubernetes Load-Balancer check page</H1>
              <font color="green"><H4  ALIGN="Center">Call with sleeping time {} sec. Running  count <H1  ALIGN="Center">{}</H1></H4>""".format(color, number, str(retcount))

@application.route("/stats")
def index():
    total = count_1 + count_5 + count_10 + count_15 + count_20
    return """<font color="green"><H1  ALIGN="Center">Kubernetes Load-Balancer check page</H1>
              <font color="green"><H4  ALIGN="Center">Total calls <H1  ALIGN="Center">{}</H1></H4>""".format(str(total))

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------