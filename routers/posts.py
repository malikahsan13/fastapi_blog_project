from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, models
from database import get_db
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/", response_model=List[schemas.PostOut])
def posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts