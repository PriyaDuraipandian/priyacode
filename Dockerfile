FROM python:3.11-slim
WORKDIR /app
COPY test_script.py .
CMD ["python3", "test_script.py"]

