# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY chore_tracker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY chore_tracker/ ./chore_tracker/
COPY start_app.sh ./
COPY simple_start.sh ./

# Create directory for database
RUN mkdir -p /app/data

# Set permissions
RUN chmod +x start_app.sh simple_start.sh

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=chore_tracker/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONPATH=/app

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Start command
CMD ["./start_app.sh"]