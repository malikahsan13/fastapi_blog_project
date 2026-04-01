from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas, models, utils
from database import get_db
from wekzeug.security import generate_password_hash, check_password_hash

router = APIRouter(tags=["Authentication"])

@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db))
