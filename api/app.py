from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/personalizada')
def home_perso():
    usu = 'PASTEL DE COXINHA'
    usu2 = {'nome': 'Sarah', 'atividade': 'Teste'}

    # Dados das pessoas
    pessoas = [
        {'nome': 'Sarah', 'idade': '18', 'endereco': 'Rua 1', 'formacao': 'Engenharia'},
        {'nome': 'João', 'idade': '22', 'endereco': 'Rua 2', 'formacao': 'Medicina'},
        {'nome': 'Maria', 'idade': '25', 'endereco': 'Rua 3', 'formacao': 'Direito'},
        {'nome': 'Carlos', 'idade': '30', 'endereco': 'Rua 4', 'formacao': 'Arquitetura'}
    ]

    return render_template('home_personalizada.html', usuario=usu, p2=usu2, pessoas=pessoas)