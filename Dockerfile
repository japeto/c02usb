FROM python:3.8

WORKDIR /home
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8025
CMD ["python", "./app.py"]
