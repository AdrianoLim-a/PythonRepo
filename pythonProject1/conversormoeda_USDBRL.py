#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

apimoeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

if apimoeda.status_code  == 200:
    dicionariomoeda = apimoeda.json()
    
    if 'USDBRL' in dicionariomoeda:
        cotacao_usd_brl = dicionariomoeda['USDBRL']
        compra_usd_brl = float(cotacao_usd_brl['bid'])
        venda_usd_brl =float(cotacao_usd_brl['ask'])
        
        quantia_usd = float(input("Digite a quantia em dólares: "))
        
        total_brl_compra = quantia_usd * compra_usd_brl
        total_brl_venda = quantia_usd * venda_usd_brl
        
        total_brl_compra_formatado = f'R${total_brl_compra:.2f}'
        total_brl_venda_formatado = f'R${total_brl_venda:.2f}'
        
        print(f'Cotação de compra do Dólar (USD-BRL):{total_brl_compra_formatado}')
        print(f'Cotação de venda do  Dólar (USD-BRL):{total_brl_venda_formatado}')
        
    else:
        print("DadoS não encontrados na resposta da API. ")

else:
    (f"Erro na solicitação da API: Código de status{apimoeda.status_code}")


# In[ ]:





# In[ ]:





# In[ ]:




