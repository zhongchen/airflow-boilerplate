from airflow.utils.decorators import apply_defaults
from airflow.models import BaseOperator, SkipMixin

from hooks.something_hook import SomethingHook
from common.stringcase import snake_case


class SomethingToSomethingOperator(BaseOperator, SkipMixin):
    @apply_defaults
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(SomethingToSomethingOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        something_hook = SomethingHook()
        print(something_hook.get_hook)

        print("custom operators says hi")
        # do your thing
        return snake_case("P-a-s-s")
