FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /source
COPY . /source

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "thumbsup.main:app", "--host", "0.0.0.0", "--port", "8080"]
