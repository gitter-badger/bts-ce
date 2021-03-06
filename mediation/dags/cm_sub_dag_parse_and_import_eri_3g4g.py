import  sys
import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator

sys.path.append('/mediation/packages');

from bts import NetworkBaseLine, Utils, ProcessCMData;

bts_utils = Utils();


def parse_and_import_eri_3g4g(parent_dag_name, child_dag_name, start_date, schedule_interval):
    dag = DAG(
        '%s.%s' % (parent_dag_name, child_dag_name),
        schedule_interval=schedule_interval,
        start_date=start_date,
    )

    t1 = BashOperator(
        task_id='check_if_eri_3g4g_raw_files_exist',
        bash_command='if [ 0 -eq `ls -1 /mediation/data/cm/ericsson/3g4g/raw/in | wc -l` ]; then exit 1; fi',
        dag=dag)

    # Backup previously generate csv files from parsing
    t5 = BashOperator(
        task_id='backup_prev_eri_3g4g_csv_files',
        bash_command='mv -f /mediation/data/cm/ericsson/3g4g/parsed/in/* /mediation/data/cm/ericsson/3g4g/parsed/out/ 2>/dev/null || true',
        dag=dag)

    t2 = BashOperator(
        task_id='run_eri_3g4g_parser',
        bash_command='java -jar /mediation/bin/boda_bulkcmparser.jar /mediation/data/cm/ericsson/3g4g/raw/in /mediation/data/cm/ericsson/3g4g/parsed/in /mediation/conf/cm/eri_cm_3g4g_parser.cfg',
        dag=dag)

    # Truncate ericsson 3g4g cm tables
    def clear_eri_3g4g_cm_tables():
        bts_utils.truncate_schema_tables(schema="eri_cm_3g4g")

    t7 = PythonOperator(
        task_id='clear_eri_3g4g_cm_tables',
        python_callable=clear_eri_3g4g_cm_tables,
        dag=dag)

    # Import csv files into csv files
    t3 = BashOperator(
        task_id='import_eri_3g4g_cm_data',
        bash_command='export PGPASSWORD=password && psql -h $POSTGRES_HOST -U bodastage -d bts -a -w -f "/mediation/conf/cm/eri_cm_3g4g_loader.cfg"',
        dag=dag)

    dag.set_dependency('check_if_eri_3g4g_raw_files_exist', 'backup_prev_eri_3g4g_csv_files')
    dag.set_dependency('backup_prev_eri_3g4g_csv_files', 'run_eri_3g4g_parser')
    dag.set_dependency('run_eri_3g4g_parser', 'clear_eri_3g4g_cm_tables')
    dag.set_dependency('clear_eri_3g4g_cm_tables', 'import_eri_3g4g_cm_data')

    return dag

