from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql://cf-python:password@localhost/my_database")

Session = sessionmaker(bind=engine)
session = Session()




Base = declarative_base()

class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    engine = create_engine
    Base.metadata.create_all(engine)

tea = Recipe(
        name = "Tea",
        cooking_time = 5,
        ingredients = "Tea Leaves, Water, Sugar"
)
    
session.add(tea)
session.commit()

