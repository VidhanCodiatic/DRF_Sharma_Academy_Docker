# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# The environment variable ensures that the Python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /SharmaAcademyCode

# Set the working directory to /SharmaAcademyCode
WORKDIR /SharmaAcademyCode

# Copy the current directory contents into the container at /SharmaAcademyCode
COPY . /SharmaAcademyCode/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run Django migrations
RUN python manage.py makemigrations && python manage.py migrate

# Expose the port that Django will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
