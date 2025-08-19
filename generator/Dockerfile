# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to the nested directory 'nb'
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .


# Run uvicorn to serve the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]