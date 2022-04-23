import requests
from datetime import datetime
import hashlib
import json

class Marvel():
    def __init__(self,_private_key,_public_key):
        self.__url = "http://gateway.marvel.com/v1/public/characters"
        self.__private_key = _private_key
        self.__public_key = _public_key

    def __get_url_data(self,lista):
        for element in lista:
            if 'http://marvel.com/characters/' in element['url']:
                return element['url']
    
    def __get_image(self,HTML):
        try:
            HTML = HTML[HTML.index('img__wrapper masthead__background'):]
            HTML = HTML[HTML.index('url('):]
            HTML = HTML[HTML.index('http'):]
            HTML = HTML[:HTML.index('&')]
            return HTML
        except:
            raise IndexError('Imagem Não Encontrada!')

    def __image_hero(self,url):
        resp = requests.get(url)
        if resp.status_code == 200:
            try:
                image= self.__get_image(resp.text)
            except IndexError:
                image = ''

            return image
        else:
            raise ValueError('Url Invalida!')

    def __generate_hash(self,ts):
        _hash = str(ts)+self.__private_key+self.__public_key
        _hash = hashlib.md5(_hash.encode())
        return _hash.hexdigest()
    
    def __get_all(self,start,width):
        ts = datetime.timestamp(datetime.now())
        resp = requests.get(f'{self.__url}?orderBy=name&limit={width}&offset={start}&apikey={self.__public_key}&hash={self.__generate_hash(ts)}&ts={str(ts)}')
        data = resp.json()
        if resp.status_code == 200:
            return data
        else:
            raise ValueError(f'code: {data["code"]} message: {data["message"]}')
    
    def __filter_info_heroes(self,_heroes):
        Hs = []
        count = len(_heroes)
        for index,hero in enumerate(_heroes):
            url = self.__get_url_data(hero['urls'])
            if url:
                print(f'[INFO][MARVEL] Coletando Informacoes Do HERO ({index+1}/{count}) : {hero["name"]}')
                Id = hero['id']
                Name = hero["name"]
                Descriptions = hero["description"]
                try:
                    Image = self.__image_hero(url)
                except:
                    Image = ''
                Hs.append({'id':Id,'name':Name,'description':Descriptions,'image':Image})
        print('[INFO][MARVEL] Coleta Finalizada')
        return Hs

    def get_data(self,start,width):
        if self.__url and self.__public_key and self.__private_key:
            print('[INFO][MARVEL] Iniciando Coleta')
            try:
                data = self.__get_all(start,width)['data']
                heroes = data['results']
                return self.__filter_info_heroes(heroes)
            except ValueError as e:
                print(f'[ERROR] {e}')
                raise ValueError(e)
        else:
            if not self.__url:
                print('Key Url Não Informada')
                raise ValueError('Key Url Não Informada')
            elif not self.__public_key:
                print('Key Publica Não Informada')
                raise ValueError('Key Publica Não Informada')
            elif not self.__private_key:
                print('Key Privada Não Informada')
                raise ValueError('Key Privada Não Informada')
