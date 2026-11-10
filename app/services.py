
from app.interfaces import TaskRepositoryInterface


class TaskService:

    def __init__(
        self,
        repository: TaskRepositoryInterface
    ):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.get_all()

    def create_task(self, task_data):
        return self.repository.create(task_data)

    def get_task(self, task_id: int):
        task = self.repository.get_by_id(task_id)

        if not task:
            raise ValueError("Task not found")

        return task

    def update_task(self, task_id: int, task_data):
        task = self.repository.update(task_id, task_data)

        if not task:
            raise ValueError("Task not found")

        return task

    def delete_task(self, task_id: int):
        task = self.repository.delete(task_id)

        if not task:
            raise ValueError("Task not found")

        return True

    def complete_task(self, task_id: int):
        task = self.repository.complete(task_id)

        if not task:
            raise ValueError("Task not found")

        return task
