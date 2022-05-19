FROM python:3.10-slim-buster

COPY  . /distance

WORKDIR /distance

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --use-deprecated=legacy-resolver


RUN pip install gunicorn

CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]

EXPOSE 5000
