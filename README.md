Prática – Flask

Este projeto implementa as rotas solicitadas nas Questões 1 e 2 da atividade.

Questão 1 – Adicionar duas rotas (GET e POST)
🔹 1.a) Rota GET com variáveis na rota

Recebe dois números diretamente pela URL.

Exemplo de uso:
/soma/10/20

Retorno esperado:
A soma é 30

🔹 1.b) Rota POST recebendo dois números (formulário)

Envia dois valores usando uma requisição POST.

Campos esperados:

num1

num2

Exemplo de envio:
num1=10
num2=20

Retorno esperado:
A soma é 30

Questão 2 – Rota GET sem variáveis na URL (query string)

Agora os valores são enviados como parâmetros de consulta (query params).

Exemplo de uso:
/soma2?num1=10&num2=20

Retorno esperado:
A soma é 30

▶ Como executar

No terminal, dentro da pasta do projeto:

```
python app.py
```

A aplicação estará disponível em:
http://localhost:5000
