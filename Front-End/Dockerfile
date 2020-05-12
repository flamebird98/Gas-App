FROM python:3.9.0a6-buster
COPY . /app
WORKDIR /app
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
RUN pip install -r requirements.txt
ENV FLASK_APP=main.py
EXPOSE 5000