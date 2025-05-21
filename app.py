from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import aiRouter


app=FastAPI()
app.include_router(aiRouter.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Origin
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

@app.get("/")
def index():
    return{"Message":"API running"}

