FROM python:3.11-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir output

VOLUME /app/output

CMD ["python3", "aggregate.py"]

