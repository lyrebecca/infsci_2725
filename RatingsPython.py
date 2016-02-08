import sys
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['moviesdb']


for line in sys.stdin:
    line = line.strip()
    UserID, MovieID, Rating, Timestamp = line.split('::')
    # genre1 = genre.split('|')
    
    db.Ratings.insert({"UserID":UserID, "MovieID":MovieID, "Rating":Rating, "Timestamp":Timestamp})
    
