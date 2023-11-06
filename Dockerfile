FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r ../requirements.txt

COPY ./app ./app

COPY ./tests ./tests

ENV PROJECT_ID="hive-access-nl"  

# RUN pytest ./tests

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
