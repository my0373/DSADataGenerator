#!/usr/bin/env python3

from sqlalchemy import create_engine, text

# Create am in memory sqlite database.
engine = create_engine("sqlite+pysqlite:///:memory:",
                       echo=True,
                       future=True)


with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
