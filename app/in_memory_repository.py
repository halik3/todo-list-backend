
from app.interfaces import TaskRepositoryInterface
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


class InMemoryTaskRepository(TaskRepositoryInterface):

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def get_all(self):
        return list(self.tasks.values())

    def get_by_id(self, task_id: int):
        return self.tasks.get(task_id)

    def create(self, task_data: TaskCreate):
        task = Task(
            id=self.next_id,
            title=task_data.title,
            description=task_data.description,
            is_completed=False
        )

        self.tasks[self.next_id] = task
        self.next_id += 1

        return task

    def update(self, task_id: int, task_data: TaskUpdate):
        task = self.get_by_id(task_id)

        if not task:
            return None

        data = task_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(task, key, value)

        return task

    def delete(self, task_id: int):
        task = self.get_by_id(task_id)

        if not task:
            return None

        del self.tasks[task_id]

        return task

    def complete(self, task_id: int):
        task = self.get_by_id(task_id)

        if not task:
            return None

        task.is_completed = True

        return task
