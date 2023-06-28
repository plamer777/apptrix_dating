FROM python:3.10-slim
WORKDIR /apptrix_dating
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn -b 0.0.0.0:5000 apptrix_dating.wsgi --workers=2 --threads=2