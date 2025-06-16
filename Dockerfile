FROM tensorflow/serving as tfserving

FROM python:3.10

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY monitoring_config.txt .
COPY forestfire-prediction/ /app/forestfire-prediction/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y supervisor

COPY --from=tfserving /usr/bin/tensorflow_model_server /usr/bin/tensorflow_model_server

EXPOSE 8501
EXPOSE 5000

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
