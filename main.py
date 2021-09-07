""" Webservice para estudar estrutudas de dados python """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def rota_principal():
    """
    Para construir funçnoes, usa-se a palavra reservad DEF:
    def nome_da_funcao(args):
        return "Ola"
    """
    return "Rota Principal"

@app.route('/listas-exemplo1')
def listas_exexmplos1():
    """
    Listas em python são estruturas lineares delimitas por 
    couxetes: Ex: lista = [1,2,3,4,5]
    lista[0] = 1
    """
    lista = [1,2,3.14,'casa',5,82,'Elefante','google.com']

    return "O {0} esta na {1} que tem o endecero do {2}".format(lista[6], lista[3], lista[7])

@app.route('/lista-exemplo2/3/4/5')
def lista_exemplo2():
    """
    Cria uma lista dinamica a partir de elementos enviados pelo usuario
    """
    lista = []
    lista.append('Cleyton')
    lista.append('Mario')
    lista.append('Marcos') 
    lista.append('Gabriel')
    lista.append('Junior')
    lista.pop()
    lista.append('Maria')
    resultado = ''
    for nome in lista:
        resultado += nome + ','

    #[1,2,3,4]
    #[].pop = remove o ultimo
    return resultado
            


@app.route('/filas')
def filas_exemplos():
    
    return 'filas'

@app.route('/noticias')
def noticias():
    #noticias = [noticia1, noticia2, noticia2]
    noticia1 = {
                'titulo':'Meu primeiro dicionario em python', 
                'autor': 'Cleyton', 
                'texto': 'isso é um exemplo de dicionario'
                }

    return 'Escrito por: ' + noticia1['autor'] + ' ' + noticia1['titulo'] + ' ' '<strong>' + noticia1['texto'] + '</strong>'

if __name__ == "__main__":
    app.run(debug=True)
