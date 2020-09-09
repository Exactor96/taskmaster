from taskmaster import views

URL_RULES = [
    {'rule': '/api/tasks', 'view_func': views.tasks_list, 'methods': ['GET']},
    {'rule': '/api/tasks', 'view_func': views.create_task, 'methods': ['POST']},
    {'rule': '/api/tasks/<task_id>', 'view_func': views.get_task, 'methods': ['GET']},
    {'rule': '/api/tasks/<task_id>', 'view_func': views.update_task, 'methods': ['PUT']},
    {'rule': '/api/tasks/<task_id>', 'view_func': views.delete_task, 'methods': ['DELETE']},



    {'rule': '/', 'view_func': views.test, 'methods': ['GET']},
]
