# Use the official Python image.
FROM python:3.9

# Set the working directory in the container.
WORKDIR /app

# Install dependencies.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container.
COPY . /app/

# Expose port 8000 for the application.
EXPOSE 8000

RUN python manage.py collectstatic --noinput

# Run the Gunicorn server.
CMD ["gunicorn", "course_manager_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
