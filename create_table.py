from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class Book(Base):
       
    __tablename__ = "books"

    ISBN = Column(String, primary_key=True)
    Book_Title = Column(String, nullable=False)
    Book_Author = Column(String, nullable=False)
    Year_Of_Publication = Column(Integer, nullable=False)
    Publisher = Column(String, nullable=False)
    Image_URL_S = Column(String)
    Image_URL_M = Column(String)
    Image_URL_L = Column(String)

    def __repr__(self):
        return(f"{self.Book_Title}[{self.Book_Author}]({self.Year_Of_Publication})")    


class Rating(Base):
       
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    User_id = Column(String, nullable=False, ForeignKey=True)
    ISBN = Column(String, ForeignKey=True)
    Book_Rating = Column(Integer, nullable=False)
    

"""   def __repr__(self):return(f"{self.Book_Title}[{self.Book_Author}]({self.Year_Of_Publication})") """

class User(Base):

    __tablename__ = "users"

    User_id = Column(String, primary_key=True)
    Location = Column(String, nullable=True)
    Age = Column(Integer, nullable=True)



engine = create_engine('sqlite:///books.db')


if __name__ == "__main__":
    # Configuration de la base de données
    Base.metadata.create_all(engine)


