from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, models, utils
from database import get_db
from typing import List

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[schemas.PostOut])
def posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return [
            schemas.PostOut(
                id=getattr(post, 'id'),
                title=getattr(post, 'title'),
                content=getattr(post,'content'),
                author= getattr(post, 'owner.username')
            )
            for post in posts
        ]

@router.post("/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(utils.get_current_user)):
    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=current_user.id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return schemas.PostOut(
        id=getattr(new_post, 'id'),
        title=getattr(new_post, 'title'),
        content=getattr(new_post,'content'),
        author= getattr(current_user, 'username')
    )
    