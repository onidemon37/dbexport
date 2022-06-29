#         name,   level, published, created_on, review_count, avg_rating
# Product 1,      1,     True,      2019-07-10, 10,           4.3

from dbexport.config import Session
from dbexport.models import Product, Review

from sqlalchemy.sql import func

import json

session = Session()

reviews_statement = (
    session.query(
        Review.product_id,
        func.count("*").label("review_count"),
        func.avg(Review.rating).label("avg_rating"),
    )
    .group_by(Review.product_id)
    .subquery()
)

products = []

for product, review_count, avg_rating in session.query(
    Product, reviews_statement.c.review_count, reviews_statement.c.avg_rating
).outerjoin(reviews_statement, Product.id == reviews_statement.c.product_id):
    products.append(
        {
            "name": product.name,
            "level": product.level,
            "published": product.published,
            "created_on": str(
                product.created_on.date()
            ),  # it is a timestamp so we need to add the date()
            "review_count": review_count or 0,  # probably going to be empty, ence the 0
            "avg_rating": round(float(avg_rating), 4) if avg_rating else 0,
        }
    )

with open("product_ratings.json", "w") as f:
    json.dump(products, f, sort_keys=True, indent=4)
