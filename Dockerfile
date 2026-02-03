FROM python:3.12-slim

WORKDIR /cnpj-data-extractor

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/cnpj-data-extractor

EXPOSE 8000

CMD ["python", "-m", "app.main"]
