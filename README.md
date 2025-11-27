# Pratica-Flask

Questão 1 – Adicionar duas rotas (GET e POST)
🔹 1.a) Rota GET com variáveis na rota

Envia os valores diretamente na URL, por exemplo:
/soma/10/20

✔ Retorna:
A soma é 30

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

Questão 2 – Modificar as rotas GET para NÃO usar parâmetros na rota

Agora a rota recebe os valores via query string, assim:

/soma_query?num1=10&num2=20

▶ Como executar
python app.py

A aplicação ficará disponível em:

http://localhost:5000
