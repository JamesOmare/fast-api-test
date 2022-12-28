from fastapi import FastAPI, Path
from .src.auth_routes import auth
from .src.order_routes import order

app = FastAPI()

app.include_router(auth)
app.include_router(order)



# uvicorn main:app --reload