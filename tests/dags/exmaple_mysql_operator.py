from datetime import datetime

from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

dag = DAG(
    dag_id='example_mysql',
    start_date=datetime(2021, 1, 1),
    default_args={'mysql_conn_id': 'mysql-test'},
    tags=['example', 'mysql'],
    catchup=False,
)

# [START howto_operator_mysql]

drop_table_mysql_task = MySqlOperator(task_id='desribe_table_mysql', sql=r"""SHOW TABLES;""", dag=dag)

# [END howto_operator_mysql]

# [START howto_operator_mysql_external_file]

mysql_task = MySqlOperator(
    task_id='drop_table_mysql_external_file',
    sql='dags/repo/tests/mysql/drop_table.sql ',
    dag=dag,
)

# [END howto_operator_mysql_external_file]

drop_table_mysql_task >> mysql_task

if __name__ == "__main__":
    dag.cli()
