from flask import Flask, render_template, request, redirect, url_for
import funcionarios_db as db

app = Flask(__name__)

@app.route('/')
def listar_funcionarios():
    funcionarios = db.buscar_funcionarios()
    return render_template('lista.html', funcionarios=funcionarios)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        db.criar_funcionario(nome, email)
        return redirect(url_for('listar_funcionarios'))
    return render_template('formulario.html', acao='Adicionar')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_funcionario(id):
    funcionario = db.buscar_funcionario_por_id(id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        db.atualizar_funcionario(id, nome, email)
        return redirect(url_for('listar_funcionarios'))
    return render_template('formulario.html', acao='Editar', funcionario=funcionario)

@app.route('/deletar/<int:id>')
def deletar_funcionario(id):
    db.deletar_funcionario(id)
    return redirect(url_for('listar_funcionarios'))

if __name__ == '__main__':
    app.run(debug=True)
