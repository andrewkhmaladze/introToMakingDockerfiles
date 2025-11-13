FROM python:3.11-slim
WORKDIR /app
# Install curl for healthchecks
RUN apt-get update && apt-get install -y curl
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]