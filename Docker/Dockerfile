FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 8080

COPY app /app

CMD ["python", "app/main.py"]

