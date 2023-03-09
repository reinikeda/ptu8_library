# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./ptu8_library .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN ./manage.py collectstatic --noinput
RUN ./manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "ptu8_library.wsgi"]
