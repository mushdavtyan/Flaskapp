# Debian - Python - Flask

`docker run -d -p 80:80 --name <name> apache-flask`

Alternatively, you can use docker-compose with:

`docker-compose up -d`

 * Download the repo
 * build the image: `docker build -t apache-flask .`
 * 
#### The docker file runs through the following steps:  

 - get the latest debian image  
 - install the requirements for python and flask on debian  
 - copy over the `requirements.txt` file and run `pip install` on it  
 - This is copied separately so that the dependencies are cached and dont need to run everytime the image is rebuilt  
 - install the requirements 
 - copy over the `application.py` file  
 - copy over the application   
 - enable the new apache config file which will redirect incoming 80 port to flask 5000 localhost port 
 - dissable the default apache config file  
 - expose port 80  
 - point the container to the application directory 
 - enable apache modes
 - run apache2 
 - run flask  
