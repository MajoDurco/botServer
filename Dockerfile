FROM python:3.5-alpine

WORKDIR /usr/src

COPY constants.py requirements.txt server.py operat.py ./
COPY Makefile server_test.py operat_test.py ./
COPY bots ./bots

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python3 server.py
