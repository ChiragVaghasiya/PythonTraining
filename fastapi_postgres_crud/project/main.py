from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import engine, Base, SessionLocal
from models import Product, Customer

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with SessionLocal() as session:
        yield session


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: AsyncSession = Depends(get_db)):
    products = (await db.execute(select(Product))).scalars().all()
    customers = (await db.execute(select(Customer))).scalars().all()
    return templates.TemplateResponse("index.html", {"request": request, "products": products, "customers": customers})


@app.post("/products/create")
async def create_product(name: str = Form(...), price: float = Form(...), db: AsyncSession = Depends(get_db)):
    prod = Product(name=name, price=price)
    db.add(prod)
    await db.commit()
    await db.refresh(prod)
    return RedirectResponse(url='/', status_code=303)


@app.post("/products/update/{id}")
async def update_product(id: int, name: str = Form(...), price: float = Form(...), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == id))
    prod = result.scalar_one_or_none()
    if not prod:
        raise HTTPException(404)
    prod.name = name
    prod.price = price
    await db.commit()
    return RedirectResponse(url='/', status_code=303)


@app.post("/products/delete/{id}")
async def delete_product(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == id))
    prod = result.scalar_one_or_none()
    if not prod:
        raise HTTPException(404)
    await db.delete(prod)
    await db.commit()
    return RedirectResponse(url='/', status_code=303)


@app.post("/customers/create")
async def create_customer(name: str = Form(...), email: str = Form(...), db: AsyncSession = Depends(get_db)):
    cust = Customer(name=name, email=email)
    db.add(cust)
    await db.commit()
    await db.refresh(cust)
    return RedirectResponse(url='/', status_code=303)


@app.post("/customers/update/{id}")
async def update_customer(id: int, name: str = Form(...), email: str = Form(...), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer).where(Customer.id == id))
    cust = result.scalar_one_or_none()
    if not cust:
        raise HTTPException(404)
    cust.name = name
    cust.email = email
    await db.commit()
    return RedirectResponse(url='/', status_code=303)


@app.post("/customers/delete/{id}")
async def delete_customer(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer).where(Customer.id == id))
    cust = result.scalar_one_or_none()
    if not cust:
        raise HTTPException(404)
    await db.delete(cust)
    await db.commit()
    return RedirectResponse(url='/', status_code=303)
