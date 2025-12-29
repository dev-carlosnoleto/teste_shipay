from fastapi import FastAPI
from app.controllers import controller

app = FastAPI(title="User API", version="1.0")

# Inclui o router definido no controller
app.include_router(controller.router)
