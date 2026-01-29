from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.models.account import Account
from app.models.transaction import Transaction
from app.dependencies import get_current_user
from app.database.session import SessionLocal

router = APIRouter(prefix="/statement")

@router.get("/")
async def statement(user_id=Depends(get_current_user)):
    async with SessionLocal() as db:
        account = (await db.execute(
            select(Account).where(Account.user_id == user_id)
        )).scalar_one()

        transactions = (await db.execute(
            select(Transaction).where(Transaction.account_id == account.id)
        )).scalars().all()

        return transactions
