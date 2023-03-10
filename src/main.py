from fastapi import FastAPI, Path
from .auth_routes import auth
from .order_routes import order

app = FastAPI()

app.include_router(auth)
app.include_router(order)



# uvicorn main:app --reload