from sqlalchemy import Column, Integer, String, create_engine
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

    

# Configuration de la base de données
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)

# import

Session = sessionmaker(bind=engine)
session = Session()

def import_books_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        for row in csvreader:
            book = Book(
                ISBN=row['ISBN'],
                Book_Title=row['Book-Title'],
                Book_Author=row['Book-Author'],
                Year_Of_Publication=row['Year-Of-Publication'],
                Publisher=row['Publisher'],
                Image_URL_S=row['Image-URL-S'],
                Image_URL_M =row['Image-URL-M'],
                Image_URL_L =row['Image-URL-L']
                )
            session.add(book)
        session.commit()

# Chemin vers le fichier CSV
csv_file_path = 'data/books.csv'
import_books_from_csv(csv_file_path)
