FROM python:3.10-slim
WORKDIR /app
COPY common-lib ./common-lib
COPY notification-service ./notification-service
WORKDIR /app/notification-service
RUN pip install -r requirements.txt
EXPOSE 5004
CMD ["python", "app.py"]
