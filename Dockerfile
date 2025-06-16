FROM tensorflow/serving:latest as model

FROM python:3.10

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY forestfire-prediction/ /models/forestfire-prediction/

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8501
EXPOSE 5000

CMD ["/usr/bin/supervisord"]