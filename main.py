from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI and uv!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
 
def new_function():
    print("new")
    
def alt():
    print(2+2)
    
def alternate():
    print("this is to differentiate which branch im on")