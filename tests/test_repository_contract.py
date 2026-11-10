import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.models import Task
from app.repository import TaskRepository
from app.in_memory_repository import InMemoryTaskRepository
from app.schemas import TaskCreate, TaskUpdate
from app.services import TaskService

@pytest.fixture(
    params=["sqlalchemy", "in_memory"],
    ids=["SQLAlchemy", "InMemory"]
)
def repository(request):

    if request.param == "in_memory":
        yield InMemoryTaskRepository()
        return

    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )

    Base.metadata.create_all(bind=engine)

    TestingSession = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    db = TestingSession()

    try:
        yield TaskRepository(db)
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()

def test_repository_contract(repository):

    # CREATE
    task = repository.create(
        TaskCreate(
            title="Belajar LSP",
            description="Repository contract testing"
        )
    )

    assert task.id is not None
    assert task.title == "Belajar LSP"
    assert task.is_completed is False

    # GET ALL
    tasks = repository.get_all()
    assert len(tasks) == 1

    # GET BY ID
    found_task = repository.get_by_id(task.id)
    assert found_task is not None
    assert found_task.title == "Belajar LSP"

    # UPDATE
    updated_task = repository.update(
        task.id,
        TaskUpdate(title="Belajar SOLID")
    )

    assert updated_task.title == "Belajar SOLID"
    assert updated_task.description == "Repository contract testing"

    # COMPLETE
    completed_task = repository.complete(task.id)
    assert completed_task.is_completed is True

    # DELETE
    deleted_task = repository.delete(task.id)
    assert deleted_task is not None
    assert repository.get_by_id(task.id) is None


def test_repository_missing_task(repository):

    assert repository.get_by_id(999) is None

    assert repository.update(
        999,
        TaskUpdate(title="Tidak ditemukan")
    ) is None

    assert repository.delete(999) is None
    assert repository.complete(999) is None


def test_task_service_works_with_repository(repository):

    service = TaskService(repository)

    task = service.create_task(
        TaskCreate(title="Testing LSP")
    )

    assert task.title == "Testing LSP"

    retrieved_task = service.get_task(task.id)
    assert retrieved_task.id == task.id

    completed_task = service.complete_task(task.id)
    assert completed_task.is_completed is True

    deleted = service.delete_task(task.id)
    assert deleted is True

    with pytest.raises(ValueError, match="Task not found"):
        service.get_task(task.id)
