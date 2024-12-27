from fastapi import FastAPI
from .routers import auth_router, index_router
from fastapi.middleware.cors import CORSMiddleware
#create an instance of a fastapi app
app = FastAPI()

origins = [
    "http://localhost:1234",
    "http://localhost:3001",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include the routers to add paths to the app
app.include_router(auth_router.router)
app.include_router(index_router.router)