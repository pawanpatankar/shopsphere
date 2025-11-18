FROM python:3.10-slim
WORKDIR /app
# copy shared lib and service code (build context is project root in docker-compose)
COPY common-lib ./common-lib
COPY user-service ./user-service
WORKDIR /app/user-service
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]
