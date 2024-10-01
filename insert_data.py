# pip install pymongo
from pymongo import MongoClient

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://root:DAvLgNQHYge8EkQo@cluster0.26bu2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.app # Same name as the database on the MongoDB website.
products_collection = db.products # Same collection name on MongoDB website.

# List of dictionaries that are holding product information. Don't have to have same number of keys.
products = [
    {
        "name": "Product 1",
        "image": "/static/images/product1.jpg",
        "price": 29.99,
        "tag": "New"
    },
    {
        "name": "Product 2",
        "image": "/static/images/product2.jpg",
        "price": 49.99,
        "tag": "Discounted"
    },
    {
        "name": "Product 3",
        "image": "/static/images/product3.jpg",
        "price": 29.99,
        "tag": "Best Seller"
    }
]

products_collection.insert_many(products) # Allows you to add multiple items, in contrast to insert_one().