FROM resin/rpi-raspbian:latest

# Install Python.
# RUN apt-get update && apt-get install -y python && rm -rf /var/lib/apt/lists/*

COPY . /app

# Start blink app
CMD ["python", "/app/blink.py"]
