FROM python:3

WORKDIR /usr/src/app

COPY pingService.py .

RUN pip install Flask==1.1.2 flask-restplus==0.13.0 requests==2.25.1 Werkzeug==0.16.1

CMD ["python", "./pingService.py"]
