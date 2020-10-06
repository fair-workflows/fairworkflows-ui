FROM python:3.6
RUN apt-get update
RUN apt-get install -y graphviz default-jre
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN ./setup_nanopub.sh mkkeys -a RSA
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app/app.py"]
