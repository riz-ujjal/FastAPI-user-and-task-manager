from pydantic import BaseModel
from typing import Optional

# This is to create user id
class UserCreate(BaseModel):
    username : str

# This to create task for the user
class TaskCreate(BaseModel):

    id: int
    title: str
    status: Optional[str] = "pending"
    priority: Optional[str] = "low"
    due_date: Optional[str] = None

# To display user data
class UserResponse(BaseModel):
    user_id: int
    username: str
    created_at: str

# To display task data
class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    status: str
    priority: str
    due_date: Optional[str] = None

# To update user details
class UserUpdateGet(BaseModel):

    username : str

# To update task data
class TaskUpdatedResponse(BaseModel):
    user_id : int
    title : str
    status: Optional[str] = "pending"
    priority: Optional[str] = "low"
    due_date: Optional[str] = None

# To delete the user
class DeleteUser(BaseModel):
    id :int
    

# To delete the task
class DeleteTask(BaseModel):
    id : int