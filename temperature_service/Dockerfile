FROM python:3.8-alpine

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 5000

CMD ["python", "temperature_server.py"]