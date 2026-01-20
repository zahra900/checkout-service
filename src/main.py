from fastapi import FastAPI

app = FastAPI(title="Checkout service", version="1.0.0")



@app.get("/")
async def root():
    return {"message": "Welcome to the checkout service"}
