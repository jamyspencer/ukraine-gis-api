FROM python:3.11

COPY ./dependencies .
RUN pip install -r ./dependencies

COPY . .

EXPOSE 8000
