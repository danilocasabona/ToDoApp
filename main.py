from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos #Importa o arquivo de autenticacao

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router) #Cria a rota da API de autenticacao do arquivo auth.py
app.include_router(todos.router)
