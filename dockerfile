# Use an official Python runtime as a parent image, based on python:3.8-slim image from DockerHub
FROM python:3.8-slim 

# Set the working directory in the container to /app
WORKDIR /app 

# Copy the current directory contents into the container at /app
COPY . /app 

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt 

# Expose port 5000 for use by other parts of your system/applications
EXPOSE 5000 
EXPOSE 11434


# On container startup, run main.py with Python
CMD ["python", "main.py"]
