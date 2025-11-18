FROM python:3.10-slim
WORKDIR /app
COPY common-lib ./common-lib
COPY order-service ./order-service
WORKDIR /app/order-service
RUN pip install -r requirements.txt
EXPOSE 5003
CMD ["python", "app.py"]
