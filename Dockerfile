FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY . /src/

RUN pip install -r requirements.txt 

CMD ["python", "emuclient_server/manage.py", "migrate"]




