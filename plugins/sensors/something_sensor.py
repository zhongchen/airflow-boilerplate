from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults
from typing import Dict


class SomethingSensor(BaseSensorOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(SomethingSensor, self).__init__(*args, **kwargs)

    def poke(self, context: Dict) -> bool:
        return True
