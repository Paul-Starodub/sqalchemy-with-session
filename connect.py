from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///sample.db", echo=True)  # echo show sql query

with engine.connect() as connection:
    pass
    # result = connection.execute(text("select 'Hello'"))
    # print(result.all())
