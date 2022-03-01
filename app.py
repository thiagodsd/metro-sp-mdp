from flask import (
    Flask,
    render_template,
    request,
    url_for
)
import pandas as pd
import metro_sp_mdp.pipelines.mdp as sp_mdp


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def form_input():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        metro_from = request.form['metro_from'].lower()
        metro_to = request.form['metro_to'].lower()
    
        ruido = ["estação", "estacao", "station", "da", "de", "do"]
        for r in ruido:
            if r in metro_from:
                metro_from = metro_from.replace(r, "")
            if r in metro_to:
                metro_to = metro_to.replace(r, "")

        df = pd.read_csv("data/01_raw/metrosp_stations.csv")

        metro_from_fuzz = sp_mdp.nodes.fuzz_string(str(metro_from), df['station'])
        metro_to_fuzz = sp_mdp.nodes.fuzz_string(str(metro_to), df['station'])

        sistema = sp_mdp.nodes.Problem(df, metro_from_fuzz, metro_to_fuzz)
        solucao = sp_mdp.pipeline.resolve_mdp(sistema)

        return render_template('index.html', result=solucao['estacoes'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
