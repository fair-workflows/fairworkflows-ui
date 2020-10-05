# fairworkflows-ui
Demo web interface for fairworkflows library

# How to run
## Using docker (recommended)
```
docker build -t fairworkflows-ui .
docker run -p 5000:5000 fairworkflows-ui
```

## Using python
Install graphviz (https://graphviz.org/)

Then:
```
pip install -r requirements.txt
python app/app.py
```
