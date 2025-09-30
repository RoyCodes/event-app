# Initial Hello World from UV
# def main():
#     print("Hello from event-app!")


# if __name__ == "__main__":
#     main()

# Testing FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
