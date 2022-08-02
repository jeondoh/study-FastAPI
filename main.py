import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/users")
def get_users(limit: int):
    return {"limit": limit}


@app.get("/users2")
def get_users2(limit: Optional[int] = None):
    return {"limit": limit}


# is_admin에 yes, 1, True를 넣더라도 is_admin은 True 반환
@app.get("/users3")
def get_users3(is_admin: bool, limit: int = 100):
    return {"is_admin": is_admin, "limit": limit}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
