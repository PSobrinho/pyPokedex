from flask  import Flask, render_template

app = Flask(__name__) # Instancia, cria, a aplicação web

@app.route("/") # Define um caminho para a página

# Página criada como função
def index():
	return render_template("index.html") # Lê e carrega o arquivo html na pasta 'templates'


app.run(debug = True) # Executa a aplicação web, debugando o cógido