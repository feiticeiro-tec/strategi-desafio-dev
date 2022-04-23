from flask import current_app,request,render_template,session,abort,redirect,url_for
from servidor.database import db,Equipe,Hero,Connection
from servidor.messagens import Messagens
import contextlib

app = current_app

@app.errorhandler(404)
def page_not_found(e):
    """ Função Responsavel Por Customizar a Pagina De Error 404"""
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipe/',methods=['GET','POST'])
def equipes():
    if request.method == 'GET':
        return render_template('equipes.html',equipes=Equipe)
    else:
        name = request.form.get('name')
        if name and name.strip():
            try:
                db.session.add(Equipe(name.strip()))
                db.session.commit()
                return render_template('equipes.html',equipes=Equipe,message=Messagens.equipe_criada(name),message_color='green')
            except:
                db.session.rollback()
                return render_template('equipes.html',equipes=Equipe,message=Messagens.equipe_existe(name),message_color='red')
        return render_template('equipes.html',equipes=Equipe,message=Messagens.nome_de_equipe_nao_informado(),message_color='red')


@app.route('/equipe/editar',methods=['GET','POST'])
def equipe_editar():
    Id = request.args.get('Id') or session.get('equipe_id')
    if Id and Id.isnumeric():
        session['equipe_id'] = Id
        equipe = Equipe.query.get(int(Id))
        
        if equipe:
            if request.method == 'GET':
                hero_name = request.args.get('hero-name')
                if hero_name:
                    heroes = Hero.query.filter(Hero.name.contains(hero_name)).all()
                    return render_template('equipe_editar.html',equipe=equipe,heroes=heroes)
                else:
                    return render_template('equipe_editar.html',equipe=equipe)
            else:
                equipe_id = request.form.get('equipe_id')
                if equipe_id and equipe_id.isnumeric():
                    equipe = Equipe.query.get(int(equipe_id))
                    for connection in equipe.connections:
                        with contextlib.suppress():
                            db.session.delete(connection)
                            db.session.commit()
                    with contextlib.suppress():
                        db.session.delete(equipe)
                        db.session.commit()
                    return redirect(url_for('equipes'))
                hero_id = request.form.get('hero_id')
                if hero_id and hero_id.isnumeric():
                    hero = Hero.query.get(int(hero_id))
                    if hero:
                        action = request.form.get('action')
                        if action in ('0','1'):
                            if action == '1':
                                if not Connection.query.filter(Connection.hero_id == hero.id).filter(Connection.equipe_id == equipe.id).first():
                                    db.session.add(Connection(hero.id,equipe.id))
                                    db.session.commit()
                                    return render_template('equipe_editar.html',equipe=equipe,message=Messagens.heroi_entrou_na_equipe(hero.name),message_color='green')
                                else:
                                    return render_template('equipe_editar.html',equipe=equipe,message=Messagens.heroi_ja_esta_na_equipe(hero.name),message_color='red')
                            else:
                                connection_hero = Connection.query.filter(Connection.hero_id == hero.id).filter(Connection.equipe_id == equipe.id).first()
                                if connection_hero:
                                    db.session.delete(connection_hero)
                                    db.session.commit()
                                    return render_template('equipe_editar.html',equipe=equipe,message=Messagens.heroi_expulso_da_equipe(hero.name),message_color='green')
                                else:
                                    return render_template('equipe_editar.html',equipe=equipe,message=Messagens.heroi_nao_esta_na_equipe(hero.name),message_color='red')
                        else:
                            return render_template('equipe_editar.html',equipe=equipe,message=Messagens.acao_nao_existe(),message_color='red')
                    else:
                        return render_template('equipe_editar.html',equipe=equipe,message=Messagens.heroi_nao_existe(),message_color='red')
                else:
                    return render_template('equipe_editar.html',equipe=equipe)
        
    return abort(404)

@app.route('/equipe/view/')
def equipe_view():
    Id = request.args.get('Id')
    if Id and Id.isnumeric():
        equipe = Equipe.query.get(int(Id))
        heroes = equipe.get_workers()
        return render_template('view_equipe.html',equipe=equipe,heroes=heroes)
    return abort(404)