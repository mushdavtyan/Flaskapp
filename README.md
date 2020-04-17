# Debian - Python - Mod_Wsgi

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
 - copy over the application config file for apache  
 - copy over the `.wsgi` file. This is the entrypoint for our application  
 - copy over the `run.py` file  
 - copy over the application  
 - enable the new apache config file and headers   
 - dissable the default apache config file  
 - expose port 80  
 - point the container to the application directory  
 - the run command. 
