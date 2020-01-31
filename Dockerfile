# Use python3 runtime as base image
FROM python:3

LABEL maintainer="Yareli Morán <yarelilys@gmail.com>" \
      description=" "

# Set working directory to
WORKDIR /home/ever/Documents/Cluster_iris_req

# From local machine to the container path
COPY . /home/ever/Documents/Cluster_iris_req

# Install the required libraries
RUN pip install -r requirements.txt

# Run Cluster3_iris.py when the containerlaunches
CMD ["python", "Cluster3_iris.py"]
