FROM resin/rpi-raspbian:wheezy
# Install Python.
RUN apt-get update \
	&& apt-get install -y python \
	# Remove package lists to free up space
	&& rm -rf /var/lib/apt/lists/*

COPY . /app

CMD ["python", "/app/blink.py"]
