import sys
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['moviesdb']


for line in sys.stdin:
    line = line.strip()
    ID, title, genre = line.split('::')
    genre1 = genre.split('|')
    
    db.Movie.insert({"title":title, "ID":ID, "genre":genre1})

    
