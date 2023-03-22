FROM python:alpine

WORKDIR /app

COPY . .

CMD ["python", "tc_Login.py"]