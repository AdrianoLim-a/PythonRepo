#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests

apimoeda = requests.get("https://economia.awesomeapi.com.br/last/JPY-BRL")

if apimoeda.status_code  == 200:
    dicionariomoeda = apimoeda.json()
    
    if 'JPYBRL' in dicionariomoeda:
        cotacao_jpy_brl = dicionariomoeda['JPYBRL']
        compra_jpy_brl = float(cotacao_jpy_brl['bid'])
        venda_jpy_brl =float(cotacao_jpy_brl['ask'])
        
        quantia_jpy = float(input("Digite a quantia em Yenes: "))
        
        total_brl_compra = quantia_jpy * compra_jpy_brl
        total_brl_venda = quantia_jpy * venda_jpy_brl
        
        total_brl_compra_formatado = f'R${total_brl_compra:.2f}'
        total_brl_venda_formatado = f'R${total_brl_venda:.2f}'
        
        print(f'Cotação de compra do Iene (JPY-BRL):{total_brl_compra_formatado}')
        print(f'Cotação de venda do  Iene (JPY-BRL):{total_brl_venda_formatado}')
        
    else:
        print("DadoS não encontrados na resposta da API. ")

else:
    (f"Erro na solicitação da API: Código de status{apimoeda.status_code}")


# In[ ]:





# In[ ]:




