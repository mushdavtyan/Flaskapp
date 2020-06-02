############################################################
# Dockerfile to build Flask App
############################################################

FROM debian:latest
MAINTAINER Mushegh Davtyan

RUN apt-get update && apt-get install -y apache2 \
    build-essential \
    python \
    python-dev\
    python-pip \
	nano\
	mc\
        htop\
        curl\
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./app/requirements.txt /var/www/requirements.txt
#######################################################################
##            change only this line to copy application              ##
#######################################################################
COPY ./app/application.py /var/www/application.py


RUN pip install -r /var/www/requirements.txt

# Copy over the apache configuration file and enable the site
COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
RUN a2ensite apache-flask
RUN a2enmod headers
RUN a2enmod proxy
RUN a2enmod proxy_http



RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf


EXPOSE 80


ENTRYPOINT  service apache2 start && FLASK_APP=/var/www/application.py flask run
