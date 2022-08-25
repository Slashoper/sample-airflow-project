"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': '邓祥虎',
}

with DAG(
    dag_id='example_bash_operator_dxh',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example', 'shell'],
    params={"example_key": "example_value"},
) as dag:

  

    # [START howto_operator_bash]
    run_test = BashOperator(
        task_id='test',
        bash_command='ifconfig ',
    )
    # [END howto_operator_bash]


if __name__ == "__main__":
    dag.cli()
