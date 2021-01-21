from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class City(BaseModel):
    name: str
    timezone: str


db = []


@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/cities')
def get_cities():
    if bool(db):
        return db
    else:
        return 'No city found'


@app.get('/cities/{city_id}')
def get_city_by_id(city_id: int):
    return db[city_id-1]


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return 'Deleted'
