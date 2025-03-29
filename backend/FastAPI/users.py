from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Entidad User
class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    
user_list = [User(id=1,username="vvparra.19",email="victoriaparrafranco@gmail.com",password="123456"),
            User(id=2,username="vvparra.19",email="victoriaparrafranco@gmail.com",password="123456"),
            User(id=3,username="vvparra.19",email="victoriaparrafranco@gmail.com",password="123456")]

@app.get("/users")
async def users():
    return user_list

@app.get("/usersjson")
async def usersjson():
    return {"user_list": user_list}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        user = filter(lambda user: user.id == user_id, user_list)
        return list(user)
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/usersquery")
async def get_user(user_id: int):
    return search_user(user_id)

def search_user(user_id: int):
    try:
        user = filter(lambda user: user.id == user_id, user_list)
        return list(user)
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/users/create", response_model= User, status_code=201)
async def create_user(user: User):
    if not search_user(user.id):
        user_list.append(user)
        return {"message": "User created successfully", "user": user}
    else:
        raise HTTPException(status_code=404, detail="User already exists")
    
@app.put("/users/update")
async def update_user(user: User):
    try:
        for i, u in enumerate(user_list):
            if u.id == user.id:
                user_list[i] = user
                return {"message": "User updated successfully", "user": user}
        return {"error": "User not found"}
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int):
    try:
        for i, u in enumerate(user_list):
            if u.id == user_id:
                del user_list[i]
                return {"message": "User deleted successfully"}
        return {"error": "User not found"}
    except Exception as e:
        return {"error": str(e)}