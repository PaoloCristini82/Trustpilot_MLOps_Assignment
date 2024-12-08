# Use Python 3.12.8 as base image
FROM python:3.12.8-slim

# Set working directory in the container
WORKDIR /app

# ________________________
# Install app dependencies

# Libraries
COPY /app/requirements.txt .
RUN pip install -r requirements.txt

# Repo functions
COPY /scr/data/data_preprocess.py .
COPY /scr/models/predict.py .

# Copy app's main file
COPY app/main.py .

# Copy artifact
COPY scr/models/artifacts/model_pipeline.pkl .

# Set environment variables
ENV RUNNING_IN_DOCKER=true

# Expose port 5000 for Flask API
EXPOSE 5000

# Command to run the API
CMD ["python", "main.py"]
