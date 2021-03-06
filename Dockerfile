FROM python:3

#ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY webapp .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
