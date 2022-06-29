FROM python:3.7-alpine

WORKDIR /app/

RUN mkdir /app/logs/

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

RUN ["python", "mqtt_pub.py", "--conf", "pub_conf.json", "--data", "data.json"]


