from servidor import create_app
from servidor.database import db,Hero
from marvel import Marvel
import sys
from time import sleep
import os

class Manager():
    def __init__(self):
        name = str(__file__)
        self.name = name[name.rfind('/')+1:]
    def run(self):
        commands = list(sys.argv)
        commands.pop(commands.index(self.name))
        for command in commands:
            if hasattr(self, command):
                eval(f'self.{command}()')

    def create_db(self):
        try:
            app = create_app()
            with app.app_context():
                db.create_all()
                print('[MANAGER][CREATE DB] TRUE')
        except:
            print('[MANAGER][CREATE DB] FALSE')
        
    def update_heroes(self):
        try:
            _public_key = os.environ.get('X_PUBLIC_KEY')
            _private_key = os.environ.get('X_PRIVATE_KEY')
            app = create_app()
            marvel = Marvel(_private_key,_public_key)
            for start in range(1,99999,100):
                data = marvel.get_data(start, 100)
                print('[MANAGER][UPDATE] COLETADO!')
                if len(data) == 0:
                    break
                for hero in data:
                    with app.app_context():
                        _hero = Hero.query.filter_by(id_hero=hero['id']).first()
                        if _hero:
                            if _hero.name != hero['name']:
                                _hero.name = hero['name']
                            if _hero.image != hero['image']:
                                _hero.image = hero['image']
                            print(f'[MANAGER][UPDATE] HEROI [{hero["name"]}] UPDATE NAME E IMAGE')
                        else:
                            try:
                                db.session.add(Hero(hero['id'],hero['name'],hero['image']))
                                db.session.commit()
                                print(f'[MANAGER][UPDATE] HEROI [{hero["name"]}] ADICIONADO COM SUCESSO!')
                            except:
                                db.session.rollback()
                                print('[MANAGER][ERROR] ROLLBACK')
                print('[MANAGER][ANTI BLOCK] ESPERANDO 30 SEGUNDOS ANTES DE IR PARA O PROXIMO')
                sleep(30)
        except:
            print('[MANAGER][UPDATE] FINALIZADO!')

if __name__ == '__main__':
    Manager().run()