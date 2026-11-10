# ToDo List API

REST API untuk mengelola daftar tugas harian yang dibangun menggunakan **FastAPI**, **SQLAlchemy**, dan **SQLite**. Proyek ini juga menerapkan prinsip **SOLID** untuk menghasilkan kode yang lebih terstruktur, mudah dikembangkan, dan mudah diuji.

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

## Struktur Proyek

```text
todo-list-backend/
├── app/
│   ├── routers/
│   │   └── tasks.py
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   ├── interfaces.py
│   ├── in_memory_repository.py
│   ├── main.py
│   ├── models.py
│   ├── repository.py
│   ├── schemas.py
│   └── services.py
├── tests/
│   ├── test_tasks.py
│   ├── test_in_memory_repository.py
│   └── test_repository_contract.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Arsitektur Aplikasi

Proyek ini menggunakan pemisahan tanggung jawab antara beberapa lapisan:

- **Router**: Menangani HTTP request, response, dan status code.
- **Dependencies**: Mengatur pembuatan dan penyediaan service serta repository.
- **Service**: Menangani logika bisnis aplikasi.
- **Repository**: Menangani operasi data menggunakan SQLAlchemy.
- **Interface**: Mendefinisikan kontrak yang harus dipenuhi implementasi repository.
- **Models**: Mendefinisikan struktur tabel database.
- **Schemas**: Mengatur validasi dan bentuk data request serta response.

Alur aplikasi:

```text
Client
  |
  v
Router
  |
  v
Dependencies
  |
  v
Service
  |
  v
Repository Interface
  |
  v
Repository Implementation
  |
  v
SQLite Database
```

## Penerapan Prinsip SOLID

### 1. Single Responsibility Principle (SRP)

Setiap komponen memiliki tanggung jawab masing-masing.

Contohnya:
- Router menangani HTTP.
- Service menangani logika bisnis.
- Repository menangani akses database.
- Dependencies menangani pembuatan objek dan dependency injection.

### 2. Open/Closed Principle (OCP)

Aplikasi mendukung lebih dari satu implementasi repository, yaitu:

- `TaskRepository`: Menggunakan SQLAlchemy.
- `InMemoryTaskRepository`: Menyimpan data di memori.

Implementasi repository baru dapat ditambahkan dengan mengikuti interface tanpa perlu mengubah logika bisnis pada `TaskService`.

### 3. Liskov Substitution Principle (LSP)

Kedua implementasi repository mengikuti kontrak `TaskRepositoryInterface`.

Pengujian kontrak dilakukan untuk memastikan keduanya dapat digunakan secara bergantian oleh `TaskService` dengan perilaku yang konsisten pada operasi yang diuji.

### 4. Interface Segregation Principle (ISP)

Interface repository dievaluasi berdasarkan kebutuhan konsumennya.

Saat ini, `TaskService` menggunakan seluruh operasi yang didefinisikan dalam `TaskRepositoryInterface`, sehingga pemisahan interface belum diperlukan.

### 5. Dependency Inversion Principle (DIP)

`TaskService` bergantung pada `TaskRepositoryInterface`, bukan pada implementasi repository SQLAlchemy secara langsung.

Dengan demikian, implementasi repository dapat diganti tanpa mengubah logika bisnis.

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

## Menjalankan Aplikasi

```bash
uvicorn app.main:app --reload
```

Dokumentasi API:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/tasks/` | Melihat semua task |
| POST | `/tasks/` | Membuat task |
| GET | `/tasks/{task_id}` | Melihat task berdasarkan ID |
| PUT | `/tasks/{task_id}` | Memperbarui task |
| DELETE | `/tasks/{task_id}` | Menghapus task |
| PATCH | `/tasks/{task_id}/complete` | Menyelesaikan task |

## Menjalankan Pengujian

Menjalankan seluruh pengujian:

```bash
pytest -v
```

Pengujian mencakup:

- Pengujian endpoint API.
- Pengujian operasi CRUD InMemory Repository.
- Pengujian kontrak repository.
- Pengujian penggunaan repository berbeda oleh TaskService.

**Hasil pengujian terakhir: 16 passed.**
