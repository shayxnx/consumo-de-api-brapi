# 📈 Banner de Ação com API Brapi.dev

Gera um banner HTML com dados de uma ação específica, usando a [API gratuita Brapi.dev](https://brapi.dev).

---

## ⚙️ Como usar

1. Instale o pacote `requests`:

   ```bash
   pip install requests
   ```

2. Edite o `app.py` para incluir:
   
   - Seu token da Brapi:
     ```python
     token = '*DIGITE SEU TOKEN AQUI*'
     ```
   - O ticker da empresa desejada (ex: `'PETR4'`, `'VALE3'`, etc.):
     ```python
     empresa =  '*DIGITE UMA OU MAIS EMPRESAS*'
     ```

3. Execute o script:

   ```bash
   python app.py
   ```

4. Um arquivo HTML será gerado com o nome `banner_<EMPRESA>.html` (ex: `banner_PETR4.html`).

5. Abra o HTML no navegador para visualizar o banner.

---

## 📂 Estrutura

```
📦 CONSUMO.API
├── app.py                ← script principal
├── banner_<EMPRESA>.html  ← banner gerado (ex: banner_PETR4.html)
└── README.md             ← este arquivo
```

---

## 🔑 Como pegar o token

- Acesse: https://brapi.dev/dashboard  
- Faça login com GitHub ou Google  
- Copie seu token gratuito e cole no script

