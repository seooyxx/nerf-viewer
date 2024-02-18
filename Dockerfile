FROM python:3.8-slim

WORKDIR /app

COPY ./js /app/
COPY main.py /app/

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]