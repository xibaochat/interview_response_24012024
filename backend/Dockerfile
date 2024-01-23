FROM python:alpine

WORKDIR /opt

COPY requirements.txt /opt

RUN pip install --upgrade pip && \
	pip install -r requirements.txt

COPY ./src /opt

EXPOSE 8000

CMD ["uvicorn", "app:app",  "--host", "0.0.0.0",  "--port",  "80", "--reload"]
