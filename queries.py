from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from create_table import Base, Book, engine


Session = sessionmaker(bind=engine)
session_queries = Session()

# nombre de livres importés
nombre_livre = session_queries.query(Book).count()
print(f"nombre de livres importés: {nombre_livre}")




