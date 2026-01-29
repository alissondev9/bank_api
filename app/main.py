from fastapi import FastAPI
from app.routes import auth, transactions, statement
from app.database.session import engine
from app.database.base import Base

app = FastAPI(title="API Bancária Assíncrona")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(statement.router)
