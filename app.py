import json

@app.route('/perfil_joao')
def perfil_joao():
    with open('livros_joao.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return render_template('perfil_joao.html', dados=dados)