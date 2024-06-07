from fastapi import FastAPI
from todo import todo_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5501", "http://52.71.209.15:8889"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {
    "msg" : "trace making"
    }

app.include_router(todo_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)