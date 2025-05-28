from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compra', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST':
        precios = {
            'cantidad_motor': 25000,
            'cantidad_dona': 23000,
            'cantidad_expert': 24000,
            'cantidad_babosa': 22000,
            'cantidad_morango': 21000,
            'cantidad_mayonesa': 20000
        }

        total = 0
        for nombre, precio in precios.items():
            cantidad = int(request.form.get(nombre, 0))
            total += cantidad * precio

        return render_template('compra.html', total=total)

    # Si alguien entra a /compra sin comprar nada, que vuelva al inicio
    return render_template('compra.html', total=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


