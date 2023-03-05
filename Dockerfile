FROM python:3.9

WORKDIR /app/
COPY . /app/

EXPOSE 3000


COPY ./app /app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


CMD uvicorn --host=0.0.0.0 --port 3000 main:app