from jose import jwt #para leer y crear tokens JWT
from passlib.context import CryptContext #forma segura de hashear y verificar contraseñas usando Passlib

SECRET_KEY = "ChuckNorris2026" #clave secreta para firmar el token
ALGORITHM = "HS256" #estándar de firma del token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#recibe  una contraseña en texto plano y reduelve un hash seguro
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#compara la contraseña que escribe el usuario con el hash guardado
def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

#crea un token
def create_token(username: str) -> str:
    payload = {"sub": username} #info que quieres guardar, en este caso el usuario que es admin
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

#verifica que el token es válido y confirma que fue firmado con tu secret_key, devuelve el usuario que esta denrto del token
def decode_token(token: str) -> str:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["sub"]