from datetime import timedelta

from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
args = {
    'owner': '叶长青',
}

with DAG(
    dag_id='example_bash_operator_hql',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['hql example'],
    params={"example_key": "example_value"},
) as dag:

    # [START howto_operator_bash]
    run_this = BashOperator(
        task_id='run_after_loop',
        bash_command="/opt/beeline/apache-hive-2.1.1-bin/bin/beeline -u  jdbc:hive2://172.26.137.230:10000 -n root -p bdp#21@/  -i /opt/airflow/dags/repo/tests/hqls/query.hql",
    )
    # [END howto_operator_bash]

    run_this

if __name__ == "__main__":
    dag.cli()