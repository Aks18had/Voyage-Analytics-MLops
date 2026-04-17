FROM python:3.10-slim

WORKDIR /app

COPY ../api /app/api
COPY ../models /app/models

RUN pip install --no-cache-dir flask joblib numpy scikit-learn

EXPOSE 5000

CMD ["python", "api/app.py"]