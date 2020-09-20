TASK_REQUIRED_FIELDS = ('name', 'start',)


def task_validation(task_data: dict) -> bool:
    for field in TASK_REQUIRED_FIELDS:
        if field not in task_data:
            return False
    return True
