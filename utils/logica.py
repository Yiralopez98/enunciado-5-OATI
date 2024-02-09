from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo.modelo import Director, Series

engine = create_engine('mysql+pymysql://root:@localhost/series_db')

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

def agregar_serie(titulo, fecha_lanzamiento, descripcion):
    nueva_serie = Series(title=titulo, release_date=fecha_lanzamiento, description=descripcion)
    session.add(nueva_serie)
    session.commit()
    print("¡Serie agregada con éxito!")

def modificar_serie(serie_id, nuevo_titulo, nuevo_fecha_lanzamiento, nueva_descripcion):
    serie = session.query(Series).filter_by(id=serie_id).first()

    if serie:
        if nuevo_titulo:
            serie.title = nuevo_titulo
        if nuevo_fecha_lanzamiento:
            serie.release_date = nuevo_fecha_lanzamiento
        if nueva_descripcion:
            serie.description = nueva_descripcion

        session.commit()
        print("¡Serie modificada con éxito!")
    else:
        print("No se encontró una serie con ese ID.")

def eliminar_serie(serie_id):
    serie = session.query(Series).filter_by(id=serie_id).first()

    if serie:
        session.delete(serie)
        session.commit()
        print("¡Serie eliminada con éxito!")
    else:
        print("No se encontró una serie con ese ID.")

def listar_series():
    series = session.query(Series).all()
    if series:
        print("Lista de series:")
        for serie in series:
            print(f"ID: {serie.id}, Título: {serie.title}, Fecha de lanzamiento: {serie.release_date}, Descripción: {serie.description}")
    else:
        print("No hay series disponibles.")
