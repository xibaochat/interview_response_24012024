from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from health import router as health_router
from router import router as main_router

app = FastAPI()

origins = ['*']


app.include_router(health_router)
app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
