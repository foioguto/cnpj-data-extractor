FROM python:3.12-slim

WORKDIR /automation-trainee

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/automation-trainee

EXPOSE 8000

CMD ["python", "-m", "app.main"]
