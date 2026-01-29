from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.user import UserCreate, Token
from app.models.user import User
from app.models.account import Account
from app.core.security import hash_password, verify_password, create_access_token
from app.database.session import SessionLocal
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    async with SessionLocal() as db:
        new_user = User(username=user.username, password=hash_password(user.password))
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        account = Account(user_id=new_user.id)
        db.add(account)
        await db.commit()

        return {"message": "Usuário criado com sucesso"}

@router.post("/login", response_model=Token)
async def login(user: UserCreate):
    async with SessionLocal() as db:
        result = await db.execute(select(User).where(User.username == user.username))
        db_user = result.scalar_one_or_none()

        if not db_user or not verify_password(user.password, db_user.password):
            return {"error": "Credenciais inválidas"}

        token = create_access_token(
            {"sub": db_user.id},
            ACCESS_TOKEN_EXPIRE_MINUTES
        )
        return {"access_token": token}
