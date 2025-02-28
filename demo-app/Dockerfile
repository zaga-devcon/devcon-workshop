# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Expose port for Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
