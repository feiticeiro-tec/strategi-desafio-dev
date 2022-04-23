from servidor.database import db

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer,primary_key = True)
    id_hero = db.Column(db.Integer,unique = True)
    name = db.Column(db.String)
    image = db.Column(db.Text)
    connections = db.relationship('Connection',backref=db.backref('heroes'),lazy=True)
    def __init__(self,id_hero,name,image):
        super().__init__()
        self.id_hero = id_hero
        self.name = name
        self.image = image