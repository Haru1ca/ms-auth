FROM python:latest

# Create app directory
WORKDIR /usr/src/app

COPY main.py ./

RUN pip install flask
RUN pip install msmcauth

CMD ["python", "main.py"]
