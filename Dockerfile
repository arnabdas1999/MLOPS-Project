# Use a Python base image that supports your target OS (Debian Buster in this case)
FROM python:3.10-slim

# Set the working directory for subsequent commands
WORKDIR /app

# Copy the requirements file first to take advantage of Docker layer caching
COPY requirements.txt .

# --- System & Python Dependency Installation ---
# FIX: Combine system updates, system installs, and pip installs into a single layer.
RUN apt-get update && \
    apt-get install -y awscli && \
    pip install --no-cache-dir -r requirements.txt && \
    # Clean up the package manager cache to reduce image size
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /app

# Set the command to run when the container starts
CMD ["python3", "app.py"]