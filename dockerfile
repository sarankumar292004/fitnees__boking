# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /fitness_booking

# Copy the entire project to the container
COPY . /fitness_booking

# Create a new virtual environment inside the container
RUN python -m venv /fitness_booking/venv

# Install dependencies using the new virtual environment's pip
RUN /fitness_booking/venv/bin/pip install -r /fitness_booking/requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django server using the newly created virtual environment
CMD ["/fitness_booking/venv/bin/python", "/fitness_booking/fitness_booking/manage.py", "runserver", "0.0.0.0:8000"]