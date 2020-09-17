from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "minha"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operacao', methods=['POST', 'GET'])
def operacao():
    if not request.values.get('numero1') or not request.values.get('numero2') or not request.values.get('operacao'):
        valor_final= "Dados invalidos"
    else:
        numero1 = request.values.get('numero1')
        numero2 = request.values.get('numero2')
        operacao = request.values.get('operacao')
        if operacao == 'soma':
            valor_final = float(numero1) + float(numero2)
        elif operacao == 'subtracao':
            valor_final = float(numero1) - float(numero2)
        elif operacao == 'multiplicacao':
            valor_final = float(numero1) * float(numero2)
        elif operacao == 'divisao':
            valor_final = float(numero1) / float(numero2)
        else:
            valor_final = "Operação Invalida"

    #passando valor usando uma variavel e usandoo session
    session['valor_final'] = valor_final
    return render_template('resultado.html', valor_final=valor_final)


if __name__ == '__main__':
    app.run(debug=True)