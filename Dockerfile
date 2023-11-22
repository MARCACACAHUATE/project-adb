FROM python:3.12
RUN apt-get update
RUN apt-get install -y libmariadb3 libmariadb-dev
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=arrivalaspincheschivas
ENV DB_ENGINE=MySQL
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/