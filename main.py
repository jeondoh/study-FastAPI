import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/{user_id}")
def get_user(user_id: float, request: Request):
    print(request.path_params)
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
