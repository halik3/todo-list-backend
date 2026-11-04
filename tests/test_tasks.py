
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Todo List API"


def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Belajar Pytest",
            "description": "Menguji aplikasi ToDo List"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Belajar Pytest"
    assert response.json()["is_completed"] is False


def test_get_tasks():
    response = client.get("/tasks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id():
    create_response = client.post(
        "/tasks/",
        json={"title": "Task untuk GET"}
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create_response = client.post(
        "/tasks/",
        json={"title": "Task Lama"}
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Task Baru",
            "description": "Sudah diperbarui",
            "is_completed": False
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Task Baru"


def test_complete_task():
    create_response = client.post(
        "/tasks/",
        json={"title": "Task yang akan diselesaikan"}
    )
    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}/complete")

    assert response.status_code == 200
    assert response.json()["is_completed"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks/",
        json={"title": "Task untuk dihapus"}
    )
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
