from servidor.database import db

class Connection(db.Model):
    __tablename__ = 'connections'
    id = db.Column(db.Integer,primary_key=True)
    hero_id = db.Column(db.Integer,db.ForeignKey('heroes.id'))
    equipe_id = db.Column(db.Integer,db.ForeignKey('equipes.id'))
    def __init__(self,hero_id,equipe_id):
        super().__init__()
        self.hero_id = hero_id
        self.equipe_id = equipe_id