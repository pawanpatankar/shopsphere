FROM python:3.10-slim
WORKDIR /app
COPY common-lib ./common-lib
COPY product-service ./product-service
WORKDIR /app/product-service
RUN pip install -r requirements.txt
EXPOSE 5002
CMD ["python", "app.py"]
