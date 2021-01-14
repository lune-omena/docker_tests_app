# First Step
# set base image (host OS)
FROM python:3.6.9

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./server.py"] 

# For each instruction or command from the Dockerfile, the Docker builder
# generates an image layer and stacks it upon the previous ones
