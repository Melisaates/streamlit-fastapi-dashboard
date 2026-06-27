from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# MEMORY STORAGE
# -----------------------
items = []
points = []

# -----------------------
# MODELS
# -----------------------
class Item(BaseModel):
    text: str

class Point(BaseModel):
    x: float
    y: float

# -----------------------
# ITEMS API
# -----------------------
@app.get("/items")
def get_items():
    return items


@app.post("/items")
def add_item(item: Item):
    items.append(item.text)
    return {"message": "item added", "items": items}


# -----------------------
# POINTS API
# -----------------------
@app.get("/points")
def get_points():
    return points


@app.post("/points")
def add_point(point: Point):
    points.append({"x": point.x, "y": point.y})
    return {"message": "point added", "points": points}