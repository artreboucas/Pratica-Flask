from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

# Questão 1 - GET com variáveis na rota
@app.get("/soma/<int:num1>/<int:num2>")
def somar_get(num1, num2):
    return f"A soma é {num1 + num2}"

# Questão 1 - POST recebendo JSON
@app.post("/soma")
def somar_post():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    return {"resultado": num1 + num2}

# Questão 2 - GET usando query params
@app.get("/soma_query")
def somar_query():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "Use: /soma_query?num1=10&num2=20"
    return f"A soma é {num1 + num2}"

if __name__ == "__main__":
    app.run(debug=True)
