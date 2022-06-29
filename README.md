# dbexport
Python Tutorial as well.

- [Programming Use Cases with Python](https://learn.acloud.guru/course/eacc77f8-54c2-427f-8c5c-e32e98123f5c/dashboard)

## requirements
- SQLAlchemy
- psycopg2-binary
- postgresql database up and running

## Usage

```
pip install -e .
export DB_URL="postgresql://$DBUSER:$PASSWORD@$HOSTNAME:$PORT/$DATABASE"
```

export as json
```
python product_json.py

```

export as csv
```
python product_csv.py
```

## Python Modules - References
- [sqlalchemy](https://www.sqlalchemy.org/)
- [sqlalchemy - engine](https://docs.sqlalchemy.org/en/14/core/engines.html)
- [sqlalchemy - sessionmaker](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#creating-a-session)
- [sqlalchemy - declare mapping](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping)
- [sqlalchemy - Query API](https://docs.sqlalchemy.org/en/13/orm/query.html)
- [sqlalchemy - relashioship](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship)
- [psycopg](https://www.psycopg.org/docs/)
- [gitignore](https://github.com/github/gitignore/)
- [functools - lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [csv](https://docs.python.org/3/library/csv.html)
- [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime)
- [json](https://docs.python.org/3/library/json.html#module-json)
- [setup.py](https://github.com/navdeep-G/setup.py)
