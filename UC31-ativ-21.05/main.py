from flask import Flask, render_template
from flask import request

app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    return "Usuário {}, Curso {} e Cidade {}".format(usuario, curso,)

if __name__ == '__main__':
    app.run(debug=True)
    