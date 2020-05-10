FROM python:3.8

WORKDIR /usr/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ADD ./ ./

EXPOSE 3000

CMD ["python", "app.py"]