FROM python:3

COPY ./dependencies .
RUN pip install -r ./dependencies

COPY . .

EXPOSE 8000
CMD python3 -m uvicorn server.main:app  --host 0.0.0.0
