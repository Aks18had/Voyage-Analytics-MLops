from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def load_data():
    print("Loading data...")

def train_model():
    print("Training model...")

def save_model():
    print("Saving model...")

with DAG(
    dag_id='ml_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    task2 = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    task3 = PythonOperator(
        task_id='save_model',
        python_callable=save_model
    )

    task1 >> task2 >> task3