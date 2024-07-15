# Use an official Python runtime as a parent image
FROM python:3.11.4-slim-buster

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ALLOWED_HOSTS localhost

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    libpq-dev \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install dotenv to manage environment variables from .env file
RUN pip install python-dotenv

# Copy the .env file
COPY .env .

# Copy project files into the working directory
COPY . .

# Expose Django server port
EXPOSE 8000

# Command to run the Django server, loading environment variables from .env file
CMD ["./start.sh"]
