# ToDo List API

REST API untuk mengelola daftar tugas harian menggunakan FastAPI, SQLAlchemy, dan SQLite.

## Teknologi

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Pytest

## Fitur

- Membuat task
- Melihat seluruh task
- Melihat task berdasarkan ID
- Memperbarui task
- Menghapus task
- Menandai task selesai

## Instalasi

Clone repository:

```bash
git clone https://github.com/halik3/todo-list-backend.git
cd todo-list-backend
```

Buat virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instal dependensi:

```bash
pip install -r requirements.txt
```

## Menjalankan aplikasi

```bash
uvicorn app.main:app --reload
```

Dokumentasi API:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Menjalankan pengujian

```bash
pytest -v
```

## Endpoint API

| Method	| Endpoint					| Fungsi 					|
|-----------|---------------------------|---------------------------|
| GET		| /tasks/					| Melihat semua task		|
| POST		| /tasks/					| Membuat task 				|
| GET		| /tasks/{task_id}			| Melihat taskberdasarkan ID|
| PUT		| /tasks/{task_id}			| Memperbarui task 			|
| DELETE	| /tasks/{task_id} 			| Menghapus task			|
| PATCH 	| /tasks/{task_id}/complete | Menyelesaikan task		|
