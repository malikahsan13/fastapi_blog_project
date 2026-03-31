from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import database


models.Base.metadata.create_all(bind = database.engine)

app = FastAPI(title="My Blog App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Welcome to My Blog"}
