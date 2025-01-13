from fastapi import FastAPI
from src.api import web_router


app = FastAPI()
app.include_router(web_router)
