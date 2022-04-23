from servidor.database import db

class Equipe(db.Model):
    __tablename__ = 'equipes'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique = True)
    connections = db.relationship('Connection',backref=db.backref('equipe'),lazy=True)
    def __init__(self,name):
        super().__init__()
        self.name = name
    def get_workers(self):
        return [worker.heroes for worker in self.connections]