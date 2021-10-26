FROM python:3.9.2-buster

WORKDIR /usr/src/app

# Copy requirement files onto docker container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]