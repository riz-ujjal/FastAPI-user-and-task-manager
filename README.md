# ⚡ Smart Productivity & Routine API

A high-performance, strictly validated RESTful microservice built to act as the backend engine for frictionless task management applications. This API is designed with clean architecture principles to seamlessly power modern, minimalist frontends (ideal for dark-mode and glassmorphism UI integrations).

## 🚀 Overview

This project provides a robust relational data pipeline for user and routine management. It utilizes modern Python features to ensure strict data validation, automatic interactive documentation, and lightning-fast request routing.

### Key Features
* **Complete CRUD Architecture:** Full Create, Read, Update, and Delete capabilities for Users and Tasks.
* **Relational Data Mapping:** One-to-Many database architecture linking tasks to specific user profiles via Foreign Keys.
* **Strict Data Validation:** Utilizes Pydantic blueprints to sanitize and validate all incoming JSON payloads before they reach the database, preventing bad data and SQL injections.
* **Automated Swagger UI:** Self-generating, interactive API documentation.
* **Secure Error Handling:** Predictable `404 Not Found` and `422 Unprocessable Content` HTTP responses for missing resources or malformed requests.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.x
* **Database:** SQLite3 (Raw SQL queries with `row_factory` dict-mapping)
* **Data Validation:** Pydantic
* **Server:** Uvicorn

## 📂 Project Structure & Flow of Data
```text
├── main.py          # The core FastAPI application, routing, and business logic
├── models.py        # Pydantic blueprints for Request/Response validation
├── database.py      # SQLite3 table creation and connection logic
└── database.db      # The local SQLite vault (auto-generated)

[ The Client ] (e.g., Postman, Browser, React Frontend)
      |
      | 1. Sends JSON Request: {"username": "ujjal"}
      v
[ main.py ] (FastAPI: The Front Desk / Traffic Cop)
      |
      | 2. "Wait, check the rules before we let this in."
      v
[ models.py ] (Pydantic: The Security Guard / Blueprints)
      |
      | 3. Checks data. "Yes, it's a string. It's approved."
      v
[ main.py ] (FastAPI takes the approved data)
      |
      | 4. Generates the exact timestamp.
      | 5. "Open the vault!" (Connects via sqlite3)
      v
[ database.db ] (SQLite3: The Vault)
      |
      | 6. Data is permanently written to the hard drive.
      v
[ main.py ] (FastAPI closes the vault)
      |
      | 7. "Send a receipt to the client."
      v
[ The Client ] gets Success Response {"message": "User created!"}

```

## 💻 Local Setup & Installation
1. Clone the repository
  Bash
    git clone [https://github.com/yourusername/smart-productivity-api.git](https://github.com/riz-ujjal/FastAPI-user-and-task-manager.git)
    cd smart-productivity-api

2. Install dependencies
  Bash
    pip install fastapi uvicorn pydantic
   
3. Initialize the Database
   -> Run the database script to generate the SQLite tables and establish the schema.
    Bash
      python database.py
   
4. Start the Server
    ->Boot up the Uvicorn ASGI server with hot-reloading enabled.
   Bash
      uvicorn main:app --reload
   
5. Explore the API
  -> Open your browser and navigate to the interactive Swagger UI documentation to test the endpoints:
👉 http://127.0.0.1:8000/docs
