from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analisar', methods=['POST'])
def analisar():
    time1 = request.form['time1']
    time2 = request.form['time2']

    resultado = f"Analisando: {time1} x {time2} ⚽\n"
    resultado += f"O time '{time1}' tem chance se focar na defesa.\n"
    resultado += f"O time '{time2}' pode vencer se explorar contra-ataques."

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
