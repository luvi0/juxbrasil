import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import io 
import openpyxl

#1colocar site do TJ 
TribunaldeJustiçadoAcre	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjac/_search'
TribunaldeJustiçadeAlagoas	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjal/_search'
TribunaldeJustiçadoAmazonas =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjam/_search'
TribunaldeJustiçadoAmapá =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjap/_search'
TribunaldeJustiçadaBahia =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjba/_search'
TribunaldeJustiçadoCeará =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjce/_search'
TJdoDistritoFederaleTerritórios ='https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search'
TribunaldeJustiçadoEspíritoSanto = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjes/_search'
TribunaldeJustiçadoGoiás ='https://api-publica.datajud.cnj.jus.br/api_publica_tjgo/_search'
TribunaldeJustiçadoMaranhão = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjma/_search'
TribunaldeJustiçadeMinasGerais	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmg/_search'
TJdoMatoGrossodeSul	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjms/_search'
TribunaldeJustiçadoMatoGrosso	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmt/_search'
TribunaldeJustiçadoPará	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpa/_search'
TribunaldeJustiçadaParaíba =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjpb/_search'
TribunaldeJustiçadePernambuco	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search'
TribunaldeJustiçadoPiauí =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjpi/_search'
TribunaldeJustiçadoParaná =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjpr/_search'
TribunaldeJustiçadoRiodeJaneiro =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search'
TJdoRioGrandedoNorte =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjrn/_search'
TribunaldeJustiçadeRondônia ='https://api-publica.datajud.cnj.jus.br/api_publica_tjro/_search'
TribunaldeJustiçadeRoraima =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjrr/_search'
TribunaldeJustiçadoRioGrandedoSul =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjrs/_search'
TribunaldeJustiçadeSantaCatarina	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsc/_search'
TribunaldeJustiçadeSergipe =	'https://api-publica.datajud.cnj.jus.br/api_publica_tjse/_search'
TribunaldeJustiçadeSãoPaulo	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search'
TribunaldeJustiçadoTocantins	= 'https://api-publica.datajud.cnj.jus.br/api_publica_tjto/_search'



def Dados_de_Processo():
    st.header('Dados de Processos', divider='red')
    st.write(
        '''
    para baixar a atualização de seu processo, primeiro selecione o estado do tribunal de justiça de seu processo e após 
    coloque o número de seu processo, para iniciar o programa, clique em solicitar dados e aguardar para clicar em Baixe seu Processo
'''
    )
    processo = st.selectbox(
    "Qual Estado?",
    ["Santa Catarina","Rio Grande do Norte","Minas Gerais", "Roraima","Amapá", "Goiás","São Paulo", "Rondônia","Sergipe","Mato Grosso do Sul", "Espiríto Santo" ,"Pernambuco", "Acre", "Ceará", "Paraná", "DF", "Bahia", "Paraíba",],
    index=None,)
    st.write("Estado Selecionado:", processo)   #unidade do processo 
    if processo == "Acre":
        url = TribunaldeJustiçadoAcre
    if processo == "Ceará":
        url = TribunaldeJustiçadoCeará
    if processo == "Bahia":
        url = TribunaldeJustiçadaBahia
    if processo == "Paraíba":
        url = TribunaldeJustiçadaParaíba
    if processo == "DF":
        url = TJdoDistritoFederaleTerritórios
    if processo == "Mato Grosso do Sul":
        url = TJdoMatoGrossodeSul
    if processo == "Maranhão":
        url = TribunaldeJustiçadoMaranhão
    if processo == "Goiás":
        url = TribunaldeJustiçadoGoiás
    if processo == "São Paulo":
        url = TribunaldeJustiçadeSãoPaulo
    if processo == "Rio de Janeiro":
        url = TribunaldeJustiçadoRiodeJaneiro
    if processo == "Espiríto Santo":
        url = TribunaldeJustiçadoEspíritoSanto
    if processo == "Amapá":
        url = TribunaldeJustiçadoAmapá
    if processo == "Roraima":
        url = TribunaldeJustiçadeRoraima
    if processo == "Minas Gerais":
        url = TribunaldeJustiçadeMinasGerais
    if processo == "Amazonas":
        url = TribunaldeJustiçadoAmazonas
    if processo == "Pará":
        url = TribunaldeJustiçadoPará
    if processo == "Piauí":
        url = TribunaldeJustiçadoPiauí
    if processo == "Paraná":
        url = TribunaldeJustiçadoParaná
    if processo == "Rio Grande do Norte":
        url = TJdoRioGrandedoNorte
    if processo == "Sergipe":
        url = TribunaldeJustiçadeSergipe
    if processo == "Alagoas":
        url = TribunaldeJustiçadeAlagoas
    if processo == "Rondônia":
        url = TribunaldeJustiçadeRondônia
    if processo == "Pernambuco":
        url = TribunaldeJustiçadePernambuco
    if processo == "Santa Catarina":
        url = TribunaldeJustiçadeSantaCatarina
    NumProcesso = st.number_input("Digite o número do processo",step=None, value=None)#, placeholder="Type a number...")  
    NumProcesso = int(NumProcesso)
    st.write(NumProcesso)
    if st.button('Solicitar dados'):
        url = 'https://api-publica.datajud.cnj.jus.br/api_publica_trf1/_search' #'https://api-publica.datajud.cnj.jus.br/api_publica_tjac/_search'
 
        api_key = "APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="

        # Define o payload
        payload = json.dumps({
            "query": {
                "match": {
                    "numeroProcesso": f"{NumProcesso}"  # Alterado para usar o número de processo digitado pelo usuário
                }
            }
        })

        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()
        df = pd.json_normalize(data['hits']['hits'])
       # Criar um buffer de memória para armazenar os dados do Excel
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, header=True)
        # Converter os dados do buffer de memória em bytes
        excel_data = excel_buffer.getvalue()
        st.download_button("Baixe seu processo", excel_data, file_name='Processos.xlsx')
    
def Feedback():
    print(2)

def PROCURA_DE_PROCESSOS():
    st.header('Procura de Processos', divider='blue')
    
def main(): #páginas de navegação
    st.sidebar.title("NAVEGAÇÃO")
    opcoes = ["Procura de Processos", "Dados de Processo", "Feedback"]
    escolha = st.sidebar.selectbox("Escolha uma página", opcoes) #radio 
   
    if escolha == "Dados de Processo":
        Dados_de_Processo()
    elif escolha == "Procura de Processos":
        PROCURA_DE_PROCESSOS()    
    elif escolha == "Feedback":
        Feedback()
   
if __name__ == "__main__":
    main()
