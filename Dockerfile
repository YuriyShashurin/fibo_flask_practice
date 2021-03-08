FROM python:3.9

ENV PORT 8081

COPY ./requirements.txt /app/requirements.txt

COPY ./app/fibo.py /app/fibo.py

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "fibo.py" ]