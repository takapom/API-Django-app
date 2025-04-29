from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"こんにちは、{name}さん！"}

