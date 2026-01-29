from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.transaction import TransactionCreate
from app.models.account import Account
from app.models.transaction import Transaction
from app.dependencies import get_current_user
from app.database.session import SessionLocal

router = APIRouter(prefix="/transactions")

@router.post("/deposit")
async def deposit(data: TransactionCreate, user_id=Depends(get_current_user)):
    async with SessionLocal() as db:
        account = (await db.execute(
            select(Account).where(Account.user_id == user_id)
        )).scalar_one()

        account.balance += data.amount
        db.add(Transaction(type="deposit", amount=data.amount, account_id=account.id))
        await db.commit()
        return {"balance": account.balance}

@router.post("/withdraw")
async def withdraw(data: TransactionCreate, user_id=Depends(get_current_user)):
    async with SessionLocal() as db:
        account = (await db.execute(
            select(Account).where(Account.user_id == user_id)
        )).scalar_one()

        if account.balance < data.amount:
            raise HTTPException(status_code=400, detail="Saldo insuficiente")

        account.balance -= data.amount
        db.add(Transaction(type="withdraw", amount=data.amount, account_id=account.id))
        await db.commit()
        return {"balance": account.balance}
