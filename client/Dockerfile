FROM python:3.6

EXPOSE 5001

WORKDIR /client

COPY requirements.txt /client
RUN pip install -r requirements.txt

COPY client.py /client
CMD python client.py http://server:5000
