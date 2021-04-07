from airflow.models import TaskInstance

from operators.something_to_something_operator import SomethingToSomethingOperator


def test_execute(dag):
    task = SomethingToSomethingOperator(dag=dag, task_id="test_task")
    ti = TaskInstance(task=task, execution_date=task.start_date)
    ret = task.execute(ti.get_template_context())

    assert ret == "p_a_s_s"
