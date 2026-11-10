from abc import ABC, abstractmethod

from app.schemas import TaskCreate, TaskUpdate


class TaskRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, task_id: int):
        pass

    @abstractmethod
    def create(self, task_data: TaskCreate):
        pass

    @abstractmethod
    def update(self, task_id: int, task_data: TaskUpdate):
        pass

    @abstractmethod
    def delete(self, task_id: int):
        pass

    @abstractmethod
    def complete(self, task_id: int):
        pass
