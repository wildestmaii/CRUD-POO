from sqlalchemy import create_engine, Integer, String, Column, Double
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///capivaras.db')
db_session  = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Capivaras(Base):
    __tablename__ ='capivaras'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    peso = Column(Double)
    cidade = Column(String(40))
    sexo = Column(String(20))

    def __repr__(self):
        return '<Capivara {}>'.format(self.nome)
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
