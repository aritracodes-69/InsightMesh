# Use official slim Python base image
FROM python:3.11-slim

# Prevent .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
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
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools wheel

# Copy dependency file first to leverage Docker cache
COPY requirements.txt .

# Install requirements (skip source builds)
RUN pip install --no-cache-dir --only-binary=PyYAML -r requirements.txt

# Copy the entire project
COPY . .

# Expose port used by Streamlit
EXPOSE 8501

# Set environment variables for Streamlit (optional)
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_ENABLEXSFPROTECTION=false

# Default command: run Streamlit UI
CMD ["streamlit", "run", "streamlit_ui/app.py"]
