import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2c6af2072383d2c99b97e1a82e945ad9"
# Your Auth Token from twilio.com/console
auth_token  = "cc0d30424ba68acf27e1e48c5d3695b3" 
client = Client(account_sid, auth_token)

# Abri os 6 arquivos de execel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5519994320549", 
            from_="+15077086596",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)
