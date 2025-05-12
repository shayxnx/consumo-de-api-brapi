import requests

token = '*DIGITE SEU TOKEN AQUI*'
empresa = '*DIGITE UMA OU MAIS EMPRESAS*'
url = f'https://brapi.dev/api/quote/{empresa}?token={token}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    acao = data['results'][0]

    logo = acao['logourl']
    simbolo = acao['symbol']
    nome = acao['shortName']
    preco = acao['regularMarketPrice']
    variacao = acao['regularMarketChangePercent']
    cor = 'green' if variacao >= 0 else 'red'

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Banner {simbolo}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .container {{
                display: flex;
                justify-content: center;
                padding: 20px;
            }}
            .card {{
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                width: 120px;
                text-align: center;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            }}
            .card img {{
                max-width: 30px;
                height: auto;
                margin-bottom: 5px;
            }}
            .green {{ color: green; }}
            .red {{ color: red; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <img src="{logo}" alt="Logo">
                <h4>{simbolo}</h4>
                <p>{nome}</p>
                <p>R$ {preco:.2f}</p>
                <p class="{cor}">{variacao:.2f}%</p>
            </div>
        </div>
    </body>
    </html>
    """

    with open("banner_ACOES.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Banner gerado como 'banner_ACOES.html'")
else:
    print("Erro ao obter dados da API.")
