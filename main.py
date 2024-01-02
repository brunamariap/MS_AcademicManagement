from fastapi import FastAPI
from prisma import Prisma
from fastapi.middleware.cors import CORSMiddleware
from controllers import course, discipline, school_class, event, diary, utils


app = FastAPI(title="MS Academic Management")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course.router)
app.include_router(discipline.router)
app.include_router(school_class.router)
app.include_router(event.router)
app.include_router(diary.router)
app.include_router(utils.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
def startup():
    prisma.connect()

@app.on_event("shutdown")
def shutdown():
    prisma.disconnect()
