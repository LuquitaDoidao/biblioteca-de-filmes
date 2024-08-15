from flask import Flask, render_template, request, redirect

app = Flask(__name__)

filmes = []
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        diretor = request.form['diretor']
        ano = request.form['ano']
        id = len(filmes)
        filmes.append([id, nome, genero, diretor, ano])
        return redirect('/')
    else:
        return render_template('adicionar_filme.html')

@app.route('/editar_filme/<int:id>', methods=['GET', 'POST'])
def editar_filme(id):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        diretor = request.form['diretor']
        ano = request.form['ano']

        filmes[id] = [id, nome, genero, diretor, ano]

        return redirect('/')
    else:
        filme = filmes[id]
        return render_template('editar_filme.html', filme=filme)

@app.route('/cancelar_filme/<int:id>')
def cancelar_filme(id):
    del filmes[id]
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)