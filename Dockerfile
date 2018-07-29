FROM python:3.6.6-alpine

COPY . /slack-garbage-notify
WORKDIR /slack-garbage-notify
RUN pip3 install -r requirements.txt

CMD python3 run.py
