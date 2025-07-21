from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()

lst_fruits = []


class Item(BaseModel):
    text: str = None
    is_done: bool = False


@app.get("/")
def root():
    return {"Hello": "Word"}


@app.post("/items")
def post_fruits(item: Item):
    lst_fruits.append(item)
    return lst_fruits


@app.get("/items/{item_id}")
def get_items(item_id: int = Path(..., description="Please Enter the input No.", gt=-1, lt=10)):
    if item_id < len(lst_fruits):
        return lst_fruits[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item Not Found !!!")
