# Use the official Python image as a base
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# [production] Copy the current directory contents into the container at /app
COPY . /app

# [develop] Copy the requirements.txt file into the container
# COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your ASGI server listens on
EXPOSE 8000

# Command to run the ASGI server

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
