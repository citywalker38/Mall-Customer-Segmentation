# Use official python image from Docker Hub
FROM python:3.11

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the current directory contents into the container in /app
COPY . /app

# Install the required python packages
RUN pip install -r requirements.txt

# Expose the port streamlit user
EXPOSE 8501

# Command to run the streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]