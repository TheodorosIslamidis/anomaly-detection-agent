FROM python:3.9-slim
WORKDIR /
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
RUN python model_train.py
EXPOSE 5000
CMD ["python", "app.py"]
