from sqlalchemy import create_engine
from modelo.modelo import Base

def create_database():
    engine = create_engine('mysql+pymysql://root:@localhost/series_db')
    
    # Crea las tablas de la base de datos
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()
