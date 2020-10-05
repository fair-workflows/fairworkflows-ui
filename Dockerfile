FROM python:3.6
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y graphviz
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app/app.py"]
