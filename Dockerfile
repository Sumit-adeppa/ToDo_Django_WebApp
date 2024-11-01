FROM python:3.8-slim-buster

WORKDIR /app

copy requirement.txt  requirement.txt

RUN pip install -r requirement.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver