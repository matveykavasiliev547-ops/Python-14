import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, Column, Integer, String, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# Важно: меняем префикс драйвера на postgresql+asyncpg
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres_user:postgres_password@db:5432/jokes_db")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

class JokeDB(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

app = FastAPI()

class JokeCreate(BaseModel):
    text: str

# Асинхронный генератор сессии для Depends
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Асинхронный POST-эндпоинт
@app.post("/jokes")
async def create_joke(joke: JokeCreate, db: AsyncSession = Depends(get_db)):
    new_joke = JokeDB(text=joke.text)
    db.add(new_joke)
    await db.commit()
    await db.refresh(new_joke)
    return {"status": "Joke added!", "id": new_joke.id, "text": new_joke.text}

# Асинхронный GET-эндпоинт
@app.get("/joke")
async def get_random_joke(db: AsyncSession = Depends(get_db)):
    # Асинхронный запрос к базе через execute + scalars
    result = await db.execute(select(JokeDB).order_by(func.random()))
    random_joke = result.scalars().first()
    
    if not random_joke:
        raise HTTPException(status_code=404, detail="В базе пока нет ни одной шутки!")
    
    return {
        "id": random_joke.id,
        "joke": random_joke.text
    }