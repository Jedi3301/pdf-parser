from fastapi import FastAPI
from routes.parse import router

app = FastAPI()
app.include_router(router)
