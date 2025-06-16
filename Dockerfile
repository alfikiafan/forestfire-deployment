FROM tensorflow/serving as tfserving

FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y supervisor

COPY app.py . 
COPY monitoring_config.txt . 
COPY forestfire-prediction/ /models/model/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY --from=tfserving /usr/bin/tensorflow_model_server /usr/bin/tensorflow_model_server

EXPOSE 5000
EXPOSE 8501

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]