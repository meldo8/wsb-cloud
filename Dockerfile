FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . .

CMD ["uvicorn", "--host=0.0.0.0", "main:app", "--reload", "--workers", "1"]
