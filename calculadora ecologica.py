# Importações
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variáveis usadas para o cálculo do consumo dos aparelhos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Primeira página
@app.route('/')
def index():
    return render_template('index.html')

# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Terceira página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                          result=result_calculate(int(size), int(lights), int(device)))

# ADICIONEI: Rota para 4 parâmetros (ex: /1/1/3/3)
@app.route('/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def quatro_parametros(num1, num2, num3, num4):
    # Calcula usando sua função (usando os 3 primeiros como size, lights, device)
    resultado = result_calculate(num1, num2, num3)
    return render_template('end.html', result=resultado)

# O formulário
@app.route('/form')
def form():
    return render_template('form.html')

# Resultados do formulário
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variáveis para a coleta dos dados
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Aqui você pode salvar os dados ou enviá-los por email
    return render_template('form_result.html', 
                           name=name,
                           email=email,
                           address=address,
                           date=date)

# CORREÇÃO: Proteger o app.run()
if __name__ == '__main__':
    app.run(debug=True)
