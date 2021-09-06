# Estruturas de Dados em Python

## Listas

## Tuplas

## Dicionários

## Strings?

## Práticas - passo a passo:
- criar env
```
python3 -m venv env
```
- Inicialize o seu repositório git.
```
git init
```
- Criando um git ignore e adicionando itens a ele
```
echo "env" >> .gitignore
```
- Adicione seu arquivo ao repositório git.
```
git add .gitignore
```
- Commitando as mudanças
```
git commit -m 'Criando o arquivo .gitignore'
```
- ativar env
```
source env/bin/activate
```
ou
```
. env/bin/activate
```
- Atualizando o PIP
```
python3 -m pip install pip --upgrade
```
- Instalar dependências (PIP)
```
python3 -m pip install flask
```
- Construindo arquivo de dependências com PIP Freeze
```
python3 -m pip freeze > requirements.txt
```
- Criar aplicação 
```
- Abra seu editor de textos (ou IDE) e crie um arquivo main.py 
  como base para nossa aplicação python (Flask).
```
```
1 - Importar o flask - a class Flask
from flask import Flask
2 - Criar um objeto do tipo Flask - com a aplicação
app = Flask(__name__)
3 - Criar uma rota (Princial - /)
@app.route('/')
def rota_principal():
   return "Rota Principal"
4 - Executar a aplicação
if "__name__" == __main__:
   app.run()
```
- Executar.
- Brincar com python
