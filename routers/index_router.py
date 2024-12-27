from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
    return{"welcome to Tasktrek"}
