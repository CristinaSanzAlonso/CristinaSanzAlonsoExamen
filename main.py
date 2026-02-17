from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from auth import router as auth_router
from deps import get_current_user

from db import get_db
from models import Incidencia


app = FastAPI(
    title="FastAPI + Swagger + JWT (básico)",
    description="Login → token → endpoint protegido",
    version="1.0.0"
)

class IncidenciaCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    descripcion: str = Field(min_length=1, max_length=1000)
    

class IncidenciaResponse(IncidenciaCreate):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2

app.include_router(auth_router)

@app.get("/")
def root():
    return {"ok": True, "mensaje": "API con MySQL lista. Ve a /docs"}

@app.get("/incidencias", response_model=list[IncidenciaResponse])
def listar_incidenciass(db: Session = Depends(get_db)):
    return db.query(Incidencia).all()

@app.post("/incidencias", response_model=IncidenciaResponse, status_code=201)
def crear_incidencia(
    incidencia: IncidenciaCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(get_current_user)
):
    nuevo = Incidencia(
        titulo=incidencia.titulo,
        descripcion=incidencia.descripcion
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo




