from model.Book import Book
from pymongo import MongoClient

book = [
    Book('monalisa','davinci',2023,'Italia'),
    Book('iliada','homero',2023,'Italia'),
    Book('monalisa','davinci',2019,'Italia'),
    Book('monalisa','davinci',2019,'Italia')
]

mongoClient=MongoClient('localhost',27017)

print(mongoClient)

db = mongoClient.Book

print(db)