FROM python:3.13-slim

RUN mkdir cims1

WORKDIR /cims1

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY . /cims1/

RUN pip install -r requirements2.txt

EXPOSE 8000

CMD [ "uwsgi --http :8000 --module cims1proj.wsgi" ]


