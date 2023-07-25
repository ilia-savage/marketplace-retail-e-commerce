FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN adduser --disabled-password service-user
RUN python manage.py makemigrations

USER service-user

