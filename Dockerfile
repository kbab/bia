FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /bia
WORKDIR /bia
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
