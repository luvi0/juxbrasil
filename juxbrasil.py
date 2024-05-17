import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import io 

#colocar site do TJ 
TribunaldeJustiçadoAcre = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjac/_search'
TribunaldeJustiçadeAlagoas = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjal/_search'
TribunaldeJustiçadoAmazonas = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjam/_search'
TribunaldeJustiçadoAmapá = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjap/_search'
TribunaldeJustiçadaBahia = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjba/_search'
TribunaldeJustiçadoCeará = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjce/_search'
TJdoDistritoFederaleTerritórios = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search'
TribunaldeJustiçadoEspíritoSanto = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjes/_search'
TribunaldeJustiçadoGoiás = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjgo/_search'
TribunaldeJustiçadoMaranhão = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjma/_search'
TribunaldeJustiçadeMinasGerais = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmg/_search'
TJdoMatoGrossodeSul = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjms/_search'
TribunaldeJustiçadoMatoGrosso = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmt/_search'
TribunaldeJustiçadoPará = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpa/_search'
TribunaldeJustiçadaParaíba = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpb/_search'
TribunaldeJustiçadePernambuco = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search'
TribunaldeJustiçadoPiauí = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpi/_search'
TribunaldeJustiçadoParaná = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpr/_search'
TribunaldeJustiçadoRiodeJaneiro = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search'
TJdoRioGrandedoNorte = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrn/_search'
TribunaldeJustiçadeRondônia = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjro/_search'
TribunaldeJustiçadeRoraima = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrr/_search'
TribunaldeJustiçadoRioGrandedoSul = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrs/_search'
TribunaldeJustiçadeSantaCatarina = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsc/_search'
TribunaldeJustiçadeSergipe = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjse/_search'
TribunaldeJustiçadeSãoPaulo = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search'
TribunaldeJustiçadoTocantins = 'https://api-publica.datajud.cnj.jus.br/api_publica_tjto/_search'

#página
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
        ["Santa Catarina", "Rio Grande do Norte", "Minas Gerais", "Roraima", "Amapá", "Goiás", "São Paulo", "Rondônia", "Sergipe", "Mato Grosso do Sul", "Espiríto Santo", "Pernambuco", "Acre", "Ceará", "Paraná", "DF", "Bahia", "Paraíba"],
        index=0
    )
    st.write("Estado Selecionado:", processo)

    urls = {
        "Acre": TribunaldeJustiçadoAcre,
        "Ceará": TribunaldeJustiçadoCeará,
        "Bahia": TribunaldeJustiçadaBahia,
        "Paraíba": TribunaldeJustiçadaParaíba,
        "DF": TJdoDistritoFederaleTerritórios,
        "Mato Grosso do Sul": TJdoMatoGrossodeSul,
        "Maranhão": TribunaldeJustiçadoMaranhão,
        "Goiás": TribunaldeJustiçadoGoiás,
        "São Paulo": TribunaldeJustiçadeSãoPaulo,
        "Rio de Janeiro": TribunaldeJustiçadoRiodeJaneiro,
        "Espiríto Santo": TribunaldeJustiçadoEspíritoSanto,
        "Amapá": TribunaldeJustiçadoAmapá,
        "Roraima": TribunaldeJustiçadeRoraima,
        "Minas Gerais": TribunaldeJustiçadeMinasGerais,
        "Amazonas": TribunaldeJustiçadoAmazonas,
        "Pará": TribunaldeJustiçadoPará,
        "Piauí": TribunaldeJustiçadoPiauí,
        "Paraná": TribunaldeJustiçadoParaná,
        "Rio Grande do Norte": TJdoRioGrandedoNorte,
        "Sergipe": TribunaldeJustiçadeSergipe,
        "Alagoas": TribunaldeJustiçadeAlagoas,
        "Rondônia": TribunaldeJustiçadeRondônia,
        "Pernambuco": TribunaldeJustiçadePernambuco,
        "Santa Catarina": TribunaldeJustiçadeSantaCatarina,
    }

    url = urls.get(processo, None)

    NumProcesso = st.number_input("Digite o número do processo", step=1)
    
    if NumProcesso:
        NumProcesso = int(NumProcesso)
        st.write("Número do Processo:", NumProcesso)

        if st.button('Solicitar dados'):
            api_key = "APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="

            # payload_consultar biblioteca
            payload = json.dumps({
                "query": {
                    "match": {
                        "numeroProcesso": f"{NumProcesso}"
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

            # Criar um buffer de memória para armazenar os dados do Excel - ferramenta nova - ao invés de encher o cache com cache.data
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, header=True)
            excel_data = excel_buffer.getvalue()
            st.download_button("Baixe seu processo", excel_data, file_name='Processos.xlsx')
    else:
        st.warning("Por favor, insira um número de processo válido.")

if __name__ == "__main__":
    Dados_de_Processo()
    st.write('Desenvolvido por Otavio Viana')