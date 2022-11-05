from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

engine = create_engine('sqlite:///Agenda/', echo=True, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Agenda(Base):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    numero = Column(Integer)
    empresa = Column(String)

    def __repr__(self):
        return f'contato {self.nome}'


def insert(agenda: Agenda):  
    session.add(agenda)
    session.commit()
    print(agenda.id)

def selectById(id):
    select = pd.read_sql_query('SELECT * FROM contatos WHERE id = {}'.format(id), engine).set_index('id')
    return select

def selectByAll():
    select = pd.read_sql_query('SELECT * FROM contatos', engine)
    return select

def deleteById(id):
   engine.execute('DELETE FROM contatos WHERE id = {}'.format(id))
    
def updateById(agenda: Agenda):
   engine.execute('UPDATE contatos SET nome = \'{0}\', email = \'{1}\', numero = \'{2}\', empresa = \'{3}\' WHERE id={4}'.format(agenda.nome, agenda.email, agenda.numero, agenda.empresa, agenda.id))
   select = pd.read_sql_query('SELECT * FROM contatos WHERE id = {}'.format(agenda.id), engine).set_index('id')
   return select 

def busca(busca):
    select = pd.read_sql_query('SELECT * FROM contatos WHERE email LIKE \'%{}%\' OR nome LIKE \'%{}%\' OR empresa LIKE \'%{}%\''.format(busca,busca,busca), engine).set_index('id')
    return select

