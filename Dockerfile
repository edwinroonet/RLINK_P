FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
#RUN pip uninstall django
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
