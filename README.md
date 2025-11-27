# Pratica-Flask

Questão 1 – Adicionar duas rotas (GET e POST)
🔹 1.a) Rota GET com variáveis na rota

Envia os valores diretamente na URL, por exemplo:

/soma/10/20


✔ Retorna:

A soma é 30

Rota:

@app.get("/soma/<int:num1>/<int:num2>")
def somar_get(num1, num2):
    return f"A soma é {num1 + num2}"

🔹 1.b) Rota POST usando JSON

Enviar requisição POST com JSON:

Exemplo:
{
  "num1": 10,
  "num2": 20
}

✔ Retorna:

{
  "resultado": 30
}

Rota:

@app.post("/soma")
def somar_post():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    return {"resultado": num1 + num2}

Questão 2 – Modificar as rotas GET para NÃO usar parâmetros na rota

Agora a rota recebe os valores via query string, assim:

/soma_query?num1=10&num2=20

Rota:

@app.get("/soma_query")
def somar_query():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "Use: /soma_query?num1=10&num2=20"
    return f"A soma é {num1 + num2}"

▶ Como executar
python app.py

A aplicação ficará disponível em:

http://localhost:5000
