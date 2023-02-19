FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD ./backend/django/requirements.txt .
RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
ADD . .