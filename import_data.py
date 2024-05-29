from sqlalchemy.orm import sessionmaker
from create_table import Base, Book, Rating, User, engine 
import csv

# import

Session = sessionmaker(bind=engine)
session = Session()

def import_books_from_csv(csv_file_book_path):
    with open(csv_file_book_path, newline='', encoding='ISO-8859-1') as csvfile:
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
        # a confirmer
        session.close()

def import_ratings_from_csv(csv_file_rating_path):
    with open(csv_file_rating_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        for row in csvreader:
            rating = Rating(
                User_id=row['User-ID'],
                ISBN=row['ISBN'],
                Book_Rating=row['Book-Rating']
                )
            session.add(rating)
        session.commit()
        # a confirmer
        session.close()

def import_users_from_csv(csv_file_users_path):
    with open(csv_file_users_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        for row in csvreader:
            user = User(
                User_id=row['User-ID'],
                Location=row['Location'],
                Age=row['Age']
                )
            session.add(user)
        session.commit()
        # a confirmer
        session.close()


# Chemin vers le fichier CSV
csv_file_book_path = 'data/books.csv'
import_books_from_csv(csv_file_book_path)

csv_file_rating_path = 'data/ratings.csv'
import_ratings_from_csv(csv_file_rating_path)

csv_file_user_path = 'data/users.csv'
import_users_from_csv(csv_file_user_path)


