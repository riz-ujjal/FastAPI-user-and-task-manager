import sqlite3
from datetime import datetime

from fastapi import FastAPI, HTTPException

from models import UserCreate, TaskCreate, UserUpdateGet, TaskUpdatedResponse

app = FastAPI()

# Inserted the data of user.
@app.post("/user/")
def user_dataTable(user: UserCreate):
    now = datetime.now()
    sqlite_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO user (username, created_at) VALUES (?,?)", (user.username, sqlite_timestamp))
        conn.commit()
    except sqlite3.IntegrityError:
        #If the username already exists, SQLite throws an IntegrityError
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists.")

    conn.close()
    return {"message": f"User {user.username} created successfully!", "timestamp": sqlite_timestamp}

# Inserted the data of task
@app.post("/task/")
def task_dataTable(task: TaskCreate):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO Tasks (user_id, title, status, priority, due_date ) VALUES(?,?,?,?,?)",
                  (task.user_id, task.title, task.status, task.priority, task.due_date))
        conn.commit()
    except sqlite3.IntegrityError:
        # Catches if the user_id doesn't exist
        conn.close()
        raise HTTPException(status_code=400, detail="Invalid user_id provided.")

    c.close()
    return {"message": f"Successfully added the task {task.title}"}

# Displaying user's data
@app.get("/user-details/{user_id}")
def get_user(user_id: int):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM user WHERE id = ?", (user_id,))
    response = c.fetchone()
    conn.close()

    # Check if the user was actually found
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(response)

# Displaying task's data
@app.get("/task-details/{task_id}")
def get_task(task_id: int):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM Tasks WHERE id = ?", (task_id,))
    task = c.fetchone()
    conn.close()

    # Check if the task was found
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return dict(task)

# Updating user's details
@app.put("/update-user-details/{user_id}")
def update_userDetails(user_id: int, user: UserUpdateGet):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("UPDATE user SET username = ?", (user.username,))

    # rowcount tells us how many rows were actually updated
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found or no changes made")

    conn.commit()
    conn.close()
    return {"message": "Successfully updated user"}

# Updating task's details
@app.put("/update-task-details/{task_id}")
def update_taskDetails(task_id: int, task: TaskUpdatedResponse):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # BUG FIX: Changed WHERE user_id = ? to WHERE id = ? so it only updates this specific task
    c.execute("UPDATE Tasks SET title = ?, status = ? , priority = ? ,due_date = ? WHERE id = ?",
              (task.title, task.status, task.priority, task.due_date, task_id))

    # Check if a task was actually updated
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()
    conn.close()
    return {"message": "Successfully updated task"}

# Deleting user's details
@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("DELETE FROM user WHERE id = ?", (user_id,))

    # Check if a user was actually deleted
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    conn.commit()
    conn.close()
    return {"message": "Successfully deleted the user"}

# Deleting task's details
@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("DELETE FROM Tasks WHERE id = ?", (task_id,))

    # Check if a task was actually deleted
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()
    conn.close()
    return {"message": "Successfully deleted the task"}