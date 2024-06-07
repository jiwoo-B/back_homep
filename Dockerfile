From python:3.10

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8888

CMD python main.py