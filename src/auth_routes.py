from fastapi import APIRouter

auth = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth.get('/')
async def hello():
    return {"message": "hello"}