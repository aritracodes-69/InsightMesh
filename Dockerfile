# Use official slim Python base image
FROM python:3.11.8-slim-bullseye

# Prevent .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && apt-get dist-upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --only-binary=PyYAML -r requirements.txt

# Copy entire project
COPY . .

# ✅ Set environment variable to point to the key inside container
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/insightmesh/insightmesh-key.json

# Expose Streamlit default port
EXPOSE 8501

# Streamlit environment settings
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_ENABLEXSFPROTECTION=false

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_ui/app.py"]






