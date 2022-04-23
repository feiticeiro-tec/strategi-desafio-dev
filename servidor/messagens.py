
class Messagens():
    @staticmethod
    def equipe_criada(name):
        return f'Equipe {name} Criada Com Sucesso!'

    @staticmethod
    def equipe_existe(name):
        return f'Equipe Com o Nome [{name}] Ja Existe!'
    
    @staticmethod
    def equipe_nao_existe(name):
        return f'A Equipe [{name}] Nao Existe!'
    
    @staticmethod
    def heroi_ja_esta_na_equipe(name):
        return f'O Heroi [{name}] Ja Esta Na Equipe!'
    
    @staticmethod
    def heroi_nao_esta_na_equipe(name):
        return f'O Heroi [{name}] Nao Esta Na Equipe!'
    
    @staticmethod
    def heroi_entrou_na_equipe(name):
        return f'O Heroi [{name}] Entrou Na Equipe!'
    
    @staticmethod
    def heroi_expulso_da_equipe(name):
        return f'O Heroi [{name}] Foi Expulso Da Equipe!'
    
    @staticmethod
    def heroi_nao_existe():
        return f'O Heroi Nao Encontrado!'

    @staticmethod
    def nome_de_equipe_nao_informado():
        return f'O Nome Da Equipe Nao Foi Informado!'
    
    @staticmethod
    def acao_nao_existe():
        return f'O Acao Nao Encontrado!'
    