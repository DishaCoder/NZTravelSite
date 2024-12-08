# importing base python image
From python:3.9-slim

#setting work directory
WORKDIR /app

# copying application files
COPY . /app

# install dependencies
RUN pip -r requirements.txt

# Port selection
EXPOSE 5001

# Application file commands
CMD ["python", "app.py"]