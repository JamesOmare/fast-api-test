from fastapi import FastAPI, Path
from .auth_routes import auth
from .order_routes import order
from fastapi_jwt_auth import AuthJWT
from .schemas import Settings

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth)
app.include_router(order)



# uvicorn src.main:app --reload
# localhost:xxx/docs