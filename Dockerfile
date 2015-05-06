FROM resin/rpi-raspbian:latest

# Install Python.
RUN apt-get update && apt-get install -y python python-pip python-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install RPi.GPIO

COPY . /app

# Start blink app
CMD ["python", "/app/blink.py"]
