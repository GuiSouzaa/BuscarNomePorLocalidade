from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_excel('Planilha/PlanilhaLocalidade.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    nomes = []
    if request.method == 'POST':
        input_localidade = request.form.get('localidade', '').strip()
        if input_localidade:
            encontrados = df[df['Localidade'].str.contains(input_localidade, case=False, na=False)]
            if not encontrados.empty:
                nomes = encontrados['Nome'].tolist()

    return render_template('index.html', nomes=nomes)


if __name__ == '__main__':
    app.run(debug=True)
