FROM python:3

COPY  . .

WORKDIR /root

RUN pip install flask requests gunicorn

CMD [ "python", "./app.py" ]