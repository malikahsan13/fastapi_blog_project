from fastapi import APIRouter, Depends, HTTPException
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
    
@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(post_id : int, updated_post: schemas.PostCreate, db : Session = Depends(get_db), current_user: models.User = Depends(utils.get_current_user)):
    current_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    
    if not current_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if getattr(current_post, 'user_id') != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    current_post.title = updated_post.title
    current_post.content = updated_post.content
    
    db.commit()
    db.refresh(current_post)
    
    return schemas.PostOut(
        id= current_post.id,
        title= current_post.title,
        content= current_post.content,
        author= current_user.username
    )
    
@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db),current_user: models.User = Depends(utils.get_current_user)):
    post =db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(post)
    db.commit()
    
    return {
        "detail":"Post deleted successfully"
    }
    
@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(utils.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return schemas.PostOut(
        id= post.id,
        title= post.title,
        content= post.content,
        author= current_user.username
    )