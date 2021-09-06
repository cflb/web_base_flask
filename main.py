""" Webservice para estudar estrutudas de dados python """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def rota_principal():
    return "Rota Principal"

if __name__ == "__main__":
    app.run()
