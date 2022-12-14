FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /root
WORKDIR /root

EXPOSE 80
CMD ["python", "app.py"]
