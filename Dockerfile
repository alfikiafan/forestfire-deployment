FROM tensorflow/serving

RUN apt-get update && apt-get install -y \
    python3 python3-pip supervisor

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY monitoring_config.txt .
COPY forestfire-prediction/ /app/forestfire-prediction/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY forestfire-prediction/ /models/model/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501
EXPOSE 5000

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
