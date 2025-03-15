#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from datetime import datetime

apimoeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

if apimoeda.status_code == 200:
    dicionariomoeda = apimoeda.json()
    
    if 'USDBRL' in dicionariomoeda:
        if 'create_date' in dicionariomoeda['USDBRL']:
            data_str = dicionariomoeda['USDBRL']['create_date']
            data_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
            data_formatada = data_obj.strftime("%d/%m/%Y")
            print(f'Data do JSON formatada: {data_formatada}')
            
            hora_formatada = data_obj.strftime("%H:%M:%S")
            print(f'Hora JSON formatada: {hora_formatada}')
            
            cotacao_usd_brl = dicionariomoeda['USDBRL']
            compra_usd_brl = float(cotacao_usd_brl['bid'])
            venda_usd_brl = float(cotacao_usd_brl['ask'])
        else:
            print("Campo create_date não encontrado no JSON")
        
        quantia_usd = float(input("Digite a quantia em dólares: "))
        
        total_brl_compra = quantia_usd * compra_usd_brl
        total_brl_venda = quantia_usd * venda_usd_brl
        
        total_brl_compra_formatado = f'R${total_brl_compra:.2f}'
        total_brl_venda_formatado = f'R${total_brl_venda:.2f}'
        
        print(f'Cotação de compra do Dólar (USD-BRL): {total_brl_compra_formatado}')
        print(f'Cotação de venda do Dólar (USD-BRL): {total_brl_venda_formatado}')
        
    else:
        print("Dados não encontrados na resposta da API.")
else:
    print(f"Erro na solicitação da API: Código de status {apimoeda.status_code}")


# In[ ]:





# In[ ]:





# In[ ]:




