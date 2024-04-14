FROM python:3.9

# Set the working directory in the container
WORKDIR /IrisDeployment

# Copy the current directory contents into the container at /app
COPY . /IrisDeployment

# Install dependencies
RUN pip install --no-cache-dir flask scikit-learn

# Expose the port Flask runs on
EXPOSE 80

# Define the command to run the Flask application
CMD ["python", "main.py"]
