import asyncio

from database import engine, Base


async def reset_db():
    # this will DROP and then CREATE all tables mapped in your models
    async with engine.begin() as conn:
        print("⚠️  Dropping all tables...")
        await conn.run_sync(Base.metadata.drop_all)
        print("✅ All tables dropped.")
        print("🚀 Creating all tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("✅ All tables created.")


if __name__ == "__main__":
    asyncio.run(reset_db())
