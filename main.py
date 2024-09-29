from typing import Optional
from decimal import Decimal
from sqlmodel import(
    Relationship,
    SQLModel,
    Field,
    create_engine,
    Session,
    ForeignKey,
    select,
)
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from uvicorn import run

engine = create_engine("sqlite:///my_db.db", echo=True)

session = Session(bind=engine)
SESSION = sessionmaker(bind=engine)
app = FastAPI(debug=True)

class Point(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
        )
    x:float
    y:float

    
@app.get("/point")
def point_get()


@app.post("/point_post")
def point_post(point:Point):
    with SESSION.begin() as session:
        session.add_all(point)





def main():
    run(
        app=app
    )

main()

"""рівняння прямої на площині"""