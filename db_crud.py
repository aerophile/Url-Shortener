import password
import time
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

error_page_url = "http://sh.ubham.com/error"

def make_engine(password=password.db_password, db_name = "url_database"):
    "retruns session using connection engine for get_row function"
    engine = create_engine('mysql://root:'+ password +'@localhost/'+ db_name +'?charset=utf8&use_unicode=0', pool_recycle=3600)
    #connection = engine.connect()
    return engine


engine = make_engine()
Base = declarative_base()
Base.metadata.reflect(engine)

class Url_table(Base):
    __table__ = Base.metadata.tables['url_table']

def make_session():
    "retruns session using connection engine for get_row function"
    engine = make_engine()
    Session = sessionmaker(bind=engine)
    sesssion = Session()
    return session

def expand_url(url_extension="home"):
    "takes short_url_extesion and returns full longer url for redirect function to use"
    db_session = scoped_session(sessionmaker(bind=engine))
    results = db_session.query(Url_table).filter_by(id=url_extension)
    
    print results.count
    if results.count == 0 : #issue: Doesn't work still returns None.. temporariy solved at flask's level
        return error_page_url
    else:
        for row in results:
            return row.long_url

    
def add_url_record(url_extension,long_url,key): 
   "add url to db"
    conn = engine.connect()
    meta = MetaData()
    meta.reflect(bind=engine)
    try:
        stmt = meta.tables["url_table"].insert().values(id=url_extension,long_url=long_url,changekey=key,creation_date=time.strftime("%y-%m-%d"))
        conn.execute(stmt)
    except:
        return "error"
    return "inserted" 

def update_url_record(key,new_long_url):
    conn = engine.connect()
    meta = MetaData()
    meta.reflect(bind=engine)
    
    try:
        stmt = update(meta.tables["url_table"]).where(meta.tables["url_table"].c.changekey==key).values(long_url=new_long_url,modify_date=time.strftime("%y-%m-%d"))
        conn.execute(stmt)
    except:
        return "error"
    return "updated"
    
    

def main():
    print expand_url("hirghi")
    #print update_url_record("key1","http://google.com")
    
if __name__ == "__main__":
    main()
