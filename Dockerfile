FROM python:3.8.10-slim-buster

ENV FLASK_APP app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["flask", "run"]