# Projeto De Desafio Do Strategi Consultoria
o projeto consiste em criar equipes de herois coletado da API: http://gateway.marvel.com/v1/public/characters
# Start
## export flask - important
`pip install -r requirements.txt`  
`export FLASK_APP='servidor:create_app()`  
`flask run`

## create database - optional
`python manager.py create_db`

## update heroes - optional
`export X_PRIVATE_KEY='you key private'`  
`export X_PUBLIC_KEY='you key public'`  
`python manager.py update_heroes`
