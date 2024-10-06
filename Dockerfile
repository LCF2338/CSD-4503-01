# The base image, which can be selected from https://hub.docker.com/
FROM python:3.12-alpine

# To define the working directory
# below is the root of the base image..
WORKDIR /

# To copy the files to the working directory
# First dot below means copy everything from the directory, and second dot says create the same directory of files on the workdir with the info we have.
COPY . .

# To install the dependency. Our python is base 3.12, we must install flask.
RUN pip install flask
RUN pip install pymongo

# To open port 5000 in the container
EXPOSE 5000

# To run the app in the container. CMD gets a list of commands/arguments we need to run.
# We'll choose "python", "main.py". It's the equivalent to going into the terminal.
CMD ["python", "main.py"]

# The order of this information is important. It's usually in this order. We run after we copy the files, for example.