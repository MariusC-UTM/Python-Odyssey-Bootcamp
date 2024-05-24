from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Produs(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

items = []

@app.post("/items/", response_model=Produs)
def create_item(item: Produs):
    items.append(item)
    return item


@app.get("/items/", response_model=List[Produs])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Produs)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Produs)
def update_item(item_id: int, item: Produs):
    for index, exist_item in enumerate(items):
        if exist_item.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{item_id}", response_model=Produs)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id ==item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)