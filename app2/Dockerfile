FROM python:3.7.4

WORKDIR /app2

VOLUME [ "/app2" ]

RUN ls

RUN pip install graphene-django

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
