# INCREMENTAL PYTHON CODE FOR CREATING PUBLICATION TABLE
# SECTION 4: LECTURE: 20
# ENTER YOUR OWN VALUE IF NEEDED FOR THE SECRET_KEY VARIABLE
# ENTER YOU OWN PASSWORD FOR THE DATABASE_URI


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

## Aquí definimos la clave, etc...
app.config.update(

    SECRET_KEY='postgressqlbv5544pnArika',
    # SQLALCHEMY_DATABASE_URI, tiene la estructura:
    # SQLALCHEMY_DATABASE_URI=<database>://<user_id>:<password>@server>/<database_name>'

    SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgressqlbv5544pnArika@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

## Esta es la forma en que le pasamos la base de datos a flask: Creamos una instancia de slq alchemy con la
## aplicación de flask como parámetro
db = SQLAlchemy(app)


# PUBLICATION TABLE
""" Con SQLAlchemy podemos crear una clase que añada registros a la tabla. En realidad, 
la clase crea una tabla. Después desde consola podemos hacer:
- Importamos desde este módulo la clase de la tabla y la sesión de base de datos así:
 from db_run import Publication,db
- Crear una instancia de la tabla, por ejemploe, pub=Publication(100,"Oxford Publications")
- Lo añadimos a la sesiòn de la base de datos con db.session.add(pub)
- Lo persistimos con un commit: db.session.commit()
También podemos añadir una lista de registros de golpe con add_all:
db.session.add_all([paramount,oracle]) tanto paraomunto como oracle se han creado como instancias de la clase 
Publication previamente.df.
"""


class Publication(db.Model):
    __tablename__ = 'publication'  #Definimos el nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)  #Pasamos el nombre de la columna
    name = db.Column(db.String(80), nullable=False)  #Y de la otra

    def __init__(self,name):
        #self.id = id en versiones posteriores quita el id porque al ser primary key es más fácil que se genere automáticamente
        self.name = name

    def __repr__(self):
        #return 'The id is {}, Name is is {}'.format(self.id, self.name)
        return 'The Name is {}'.format(self.name)

# BOOK TABLE
""" Añado directamente la tabla "book" directamente desde el repo en el mismo código.
Se puede ver que el proceso de creación es el mismo y los pasos similares.

"""


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True) # Con index =True se crea un índice asociado al campo
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True) # con unique = True se obliga a que no haya duplicados.
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow()) #Pasamos como valor por defecto la fecha de hoy

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    """ Aquí se crea la relación 1- n entre la tabla publication y su clave id y esta columna
    Por este motivo, se define como una clave foránea
    """
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        """
        En el __init__ no hemos puesto ni la pub_date que  nos va a coger el valor por defecto
        ni la primary key que es el campo id porque sqlalchemy nos la genera sola. Ponemos el resto de campos.
        """

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()   # Este comando crea las tablas si no existen
    app.run(debug=True)
