FROM python:3.8-slim-buster

# Set working directory
WORKDIR /code

# Keeps Python from generating .pyc files in the container
# Turns off buffering for easier container logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update image dependencies
RUN apt-get update
RUN apt-get upgrade -y

# Install app dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements-prod.txt ./
RUN python3 -m pip install -r requirements-prod.txt

# Copy app files 
COPY . .

EXPOSE 8000