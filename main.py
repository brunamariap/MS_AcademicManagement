from fastapi import FastAPI
from prisma import Prisma
from controllers import course, discipline, school_class, event


app = FastAPI()
app.include_router(course.router)
app.include_router(discipline.router)
app.include_router(school_class.router)
app.include_router(event.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
