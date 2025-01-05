# Start from the Python image
FROM python:3.10

# Set the working directory
WORKDIR /usr/src/app

# Copy the application files from rule-engine directory
COPY . .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /usr/src/app
