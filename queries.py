from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from create_table import Base, Book, engine


Session = sessionmaker(bind=engine)
session_queries = Session()

# nombre de livres importés
#nombre_livre = session_queries.query(Book).count()
#print(f"nombre de livres importés: {nombre_livre}")

# modification affichage d un livre
# selectionner juste les 5 premiers livres et les afficher
query2 = session_queries.query(Book).order_by(Book.Year_Of_Publication.desc()).limit(3)
#print(type(query2))
for x in query2:
   print(x)
#print(f"affichage initial des 5 premiers livres : {query2}")


