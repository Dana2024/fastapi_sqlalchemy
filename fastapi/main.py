from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close


class Flavor(BaseModel):
    name: str


@app.post("/addflavor/")
def add_flavor(flavor: Flavor, db: Session = Depends(get_db)):
    flavor_model = models.Flavors()
    flavor_model.name = flavor.name

    db.add(flavor_model)
    db.commit()

    return flavor


@app.get("/flavors/")
def get_flavors(db: Session = Depends(get_db)):
    return db.query(models.Flavors).all() 
    

@app.get("/")
def home():
    return {"Hello!"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

