from flask import Flask, request

app = Flask(__name__)

# Questão 1 - GET 
@app.get("/soma/<int:num1>/<int:num2>")
def somar_get(num1, num2):
    return f"A soma é {num1 + num2}"

# Questão 1 - POST 
@app.post("/soma")
def somar_post():
    num1 = float(request.form.get("num1"))
    num2 = float(request.form.get("num2"))
    return f"A soma é {num1 + num2}"

# Questão 2 - GET 
@app.get("/soma2")
def somar_query():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    return f"A soma é {num1 + num2}"

if __name__ == "__main__":
    app.run(debug=True)
