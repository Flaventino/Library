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
#query2 = session_queries.query(Book).order_by(Book.Year_Of_Publication.desc()).limit(3)
#print(type(query2))
""" for x in query2:
   print(x) """

# affichage des livres dont le titre comporte "The hobbit"
#query3 = session_queries.query(Book).where(Book.Book_Title.like("%the Hobbit%"))
query3 = session_queries.query(Book).filter(Book.Book_Title.like("%the Hobbit%"))
for x in query3:
   print(x)

