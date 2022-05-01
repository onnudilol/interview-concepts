from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://root:password@mongo/admin")
db = client.api


# This is to cast MongoDB document _id ObjectIds to strings
# see https://www.mongodb.com/developer/quickstart/python-quickstart-fastapi/#creating-the-application
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Schema for the neighborhood collection
class NeighborhoodModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    geometry: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# Schema for the restaurant collection
class RestaurantModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    location: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# Smoke test endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Get 100 restaurants from the restaurant collection
@app.get("/restaurants", response_model=List[RestaurantModel])
async def get_restaurants():
    restaurants = await db["restaurants"].find().to_list(100)

    return restaurants


# Get 100 neighborhoods from the neighborhood collection
@app.get("/neighborhoods", response_model=List[NeighborhoodModel])
async def get_neighborhoods():
    neighborhoods = await db["neighborhoods"].find().to_list(100)
    return neighborhoods
