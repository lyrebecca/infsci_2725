import sys
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['moviesdb']


for line in sys.stdin:
    line = line.strip()
    UserID, MovieID, Tag, Timestamp = line.split('::')
   # genre1 = genre.split('|')
    
    db.Tags.insert({"UserID":UserID, "MovieID":MovieID, "Tag":Tag, "Timestamp":Timestamp})
    
