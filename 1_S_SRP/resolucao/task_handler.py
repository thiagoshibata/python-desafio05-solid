from typing import Dict

class TaskHandler:

    def create_task(task: Dict):
        print("Task criada:", task)

    def update_task(id_task:int, task_updated: Dict):
        print(f"Task: {id_task} atualizada",task_updated)

    def remove_task(id_task:int):
        print("Task removida",id_task)
        