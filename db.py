from sqlalchemy import create_engine #crea la conexion a la bbdd
from sqlalchemy.orm import sessionmaker, declarative_base #crea las sesiones y la base para deinir los modelos (tablas)

#diuce cómo conectarse a la bbdd
DATABASE_URL = "mysql+pymysql://root:ChuckNorris2025@localhost:3308/fastapi_incidentes"

#motor de conexión
engine = create_engine(DATABASE_URL, echo=True)
#sesión para la bbdd
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()