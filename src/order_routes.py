from fastapi import APIRouter

order = APIRouter(
    prefix="/orders",
    tags=['orders']
)


@order.get('/')
async def hello():
    return {"message": "hello"}