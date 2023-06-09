from .. import models, schemas, utils, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)



# To get all the posts we can use any one either this one or below one
@router.get("/", response_model = List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts


# To get all the posts we can use any one either this one or above one
# To get all the posts of particular user 
# @router.get("/", response_model = List[schemas.Post])
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     posts = db.query(models.Post).filter(models.Post.ownner_id==current_user.id).all()
#     return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.Post])
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # print(current_user.email)
    new_post = models.Post(ownner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {new_post}



@router.get("/{id}", response_model=List[schemas.Post])
def get_posts(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id: {id} was not found")
        
    # Use of foreign key with ownner_id
    
    # if post.ownner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
    #                         detail="Not authorise to requested action")
    
    return {post}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id: {id} does not exists")
    
    if post.ownner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorise to requested action")
        
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@router.put("/{id}", response_model=List[schemas.Post])
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    updated_post_query = db.query(models.Post).filter(models.Post.id == id)
    post = updated_post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id: {id} does not exists")
    
    if post.ownner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorise to requested action")
    
    updated_post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return {updated_post_query.first()}

