# This is the base image from which we build our custom image
FROM python:latest

# This created the working directory in the docker file system and NOT in my host machine 
# Only mkdir not mkdir plus cd 
WORKDIR /home/sath

# 'ENV' can be used to define the env varibles of the container of that image but its better to define 
# it in the docker-compose for easy edit 

# This copy allows us to copy the files from my host machine to the working dirctory/any place inside the docker container
COPY templates /home/sath/
COPY app.py /home/sath/

# RUN will run any Linux command on the container cli
RUN pip install Flask
RUN pip install Flask-PyMongo

#CMD is also like run BUT it is the entry point to which the application will run from.
# words seperated by , to make the command to run on terminal of the container
CMD ["python","/home/sath/app.py"]
