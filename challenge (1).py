import pandas as pd
import streamlit as st
from datetime import datetime
from io import BytesIO
import base64
import os
import io
import tempfile
@st.cache_data
def to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Comissao_processada')
    writer.save()
    excel_data = output.getvalue()
    b64 = base64.b64encode(excel_data).decode('utf-8')
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="comissao_processada.xlsx">Clique aqui para baixar o arquivo Excel</a>'
    return href
def process_commissions(relatorio):
    # Filtrar o DataFrame para linhas com 'comission_type' igual a 'spot' e 'status' igual a 'finished'
    filtro = (comissao['commission_type'] == 'spot') & (comissao['status'] == 'finished')

    # Aplicar o filtro no DataFrame
    dados_filtrados = comissao[filtro]

    # Calcular a soma total da coluna 'net' por 'partner'
    soma_total_por_partner = dados_filtrados.groupby('partner')['net'].sum().reset_index()

    # Renomear a coluna resultante para representar o total da soma
    soma_total_por_partner.rename(columns={'net': 'Total_Soma_por_Partner'}, inplace=True)
    # Calculando a soma por partner
    soma_por_partner = dados.groupby('partner')['net'].sum().reset_index()
    soma_por_partner.rename(columns={'net': 'soma_partner'}, inplace=True)

    # Merge do DataFrame original com a soma por partner
    comissao = pd.merge(dados, soma_por_partner, on='partner')

    def calculate_commission_factor(row):
        valor_soma = row['soma_partner']
        product = row['product']
        number_of_installments = row['number_of_installments']
        commission_type = row['commission_type']
    # Adicione condições com base no valor da soma
        if valor_soma >= 30000000:
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.035
                    elif commission_type == 'bonus':
                            return None
                            #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.015
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                    # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.015
                elif commission_type == 'bonus':
                        return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.03
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.03
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.03
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.015
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.015
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.015
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.015

                # Restante das condições conforme necessário
        if valor_soma >= 20000000 and valor_soma < 29999999:
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.03
                    elif commission_type == 'bonus':
                        return None
                        #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.01
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.01
                elif commission_type == 'bonus':
                    return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.025
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.025
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.03
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0125
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0125
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0125
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0125
        if valor_soma >= 10000000 and valor_soma < 19999999:
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.02
                    elif commission_type == 'bonus':
                        return None
                        #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.0075
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.0075
                elif commission_type == 'bonus':
                    return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.02
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.02
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.02
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.01
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.01
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.01
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.01
        if valor_soma >= 5000000 and valor_soma < 9999999:
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.01
                    elif commission_type == 'bonus':
                        return None
                        #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.005
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.005
                elif commission_type == 'bonus':
                    return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.015
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.015
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.015
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0075
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0075
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0075
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0075
        if valor_soma >= 3000000 and valor_soma < 4999999 :
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.005
                    elif commission_type == 'bonus':
                        return None
                        #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.0025
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.0025
                elif commission_type == 'bonus':
                    return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.01
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.01
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.01
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.005
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.005
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.005
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.005
        if valor_soma >= 2000000 and valor_soma < 2999999 :
            if product == 'FGTS | Normal':
                if number_of_installments >= 5:
                    if commission_type == 'spot':
                        return 0.0025
                    elif commission_type == 'bonus':
                        return None
                        #Flat30
            if product == 'FGTS | Flat 30':     
                if commission_type == 'spot':
                    return 0.0015
                elif commission_type == 'bonus':
                    return None # Bônus para FGTS | Flat 30
            if product == 'FGTS | Flat 50':
                # Lógica para FGTS | Flat 50
                if commission_type == 'spot':
                    return 0.0015
                elif commission_type == 'bonus':
                    return None
            if product == 'FGTS | TOP':     
                if commission_type == 'spot':
                    return 0.005
            if product == 'FGTS | VIP':     
                if commission_type == 'spot':
                    return 0.005
            if product == 'FGTS | Ouro':     
                if commission_type == 'spot':
                    return 0.005
            if product == 'INSS | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0025
            if product == 'INSS | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0025
            if product == 'INSS | BPC Loas | Normal | Novo ou Aumento':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0025
            if product == 'INSS | BPC Loas | Normal':
                if commission_type == 'spot':
                    if 36 <= number_of_installments == 84:
                        return 0.0025
    comissao['commission_factor'] = comissao.apply(calculate_commission_factor, axis=1)
    # Excluir as linhas onde 'commission_factor' está vazia 
    comissao = comissao.dropna(subset=['commission_factor'])
    # Calcula o 'commission_value' para todos os casos
    comissao['commission_value'] = comissao['commission_base'] * comissao['commission_factor']


    # Limita o valor da comissão a duas casas decimais
    comissao['commission_value'] = comissao['commission_value'].round(2)
    # Obter a data atual
    data_atual = datetime.now()

    #Formatar a data no formato desejado
    data_formatada = data_atual.strftime('%d/%m/%Y')

    #Atribuir a data formatada à coluna 'comission_date' na 'planilha'
    comissao['commission_date'] = data_formatada
    # Converter as colunas 'start' e 'disbursement' para o tipo de data
    comissao['start'] = pd.to_datetime(comissao['start'])
    comissao['disbursment'] = pd.to_datetime(comissao['disbursment'])

    #Formatar as colunas 'start' e 'disbursement' no formato desejado
    comissao['start'] = comissao['start'].dt.strftime('%d/%m/%Y')
    comissao['disbursment'] = comissao['disbursment'].dt.strftime('%d/%m/%Y')
    comissao.loc[dados['commission_type'] == 'spot', 'commission_type'] = 'challenge'
    
    return comissao_processada
def main():
    st.image("logoverde.png", width=200)
    st.title("Módulo Challenge iCred")
    data_formatada = datetime.now().strftime('%d/%m/%Y')

    uploaded_file_comissao = st.file_uploader("Selecione o arquivo de relatório de comissão", type=["xlsx", "xls"])

    if uploaded_file_comissao is not None:
        relatorio_comissao = pd.read_excel(uploaded_file_comissao)
        comissao = process_commissions(relatorio_comissao)

        # Criar um arquivo Excel temporário em memória usando BytesIO para 'comissao'
        excel_buffer_comissao = io.BytesIO()
        excel_writer_comissao = pd.ExcelWriter(excel_buffer_comissao, engine='xlsxwriter')
        comissao.to_excel(excel_writer_comissao, index=False)
        excel_writer_comissao.close()
        excel_buffer_comissao.seek(0)

        # Gerar o link de download para o arquivo Excel temporário 'comissao'
        b64_comissao = base64.b64encode(excel_buffer_comissao.read()).decode()
        href_comissao = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_comissao}" ' \
                        f'download="relatorio_comissao.xlsx">Clique aqui para baixar o relatório de comissão</a>'

        # Mostrar o link de download para 'comissao' na interface do Streamlit
        st.markdown(href_comissao, unsafe_allow_html=True)

        # Continuar com o upload e processamento do arquivo 'financeiro'
        uploaded_financeiro = st.file_uploader("Selecione o arquivo financeiro", type=["xlsx", "xls"])
        data_formatada = datetime.now().strftime('%d/%m/%Y')

        if uploaded_financeiro is not None:
            financeiro = pd.read_excel(uploaded_financeiro)

            # Função para verificar o prefixo do produto e retornar "INSS" ou "FGTS"
            def categorizar_product(product):
                if product.startswith('INSS'):
                    return 'INSS'
                else:
                    return 'FGTS'

            # Aplicar a função à coluna 'produto' para criar a nova coluna 'categoria'
            comissao['categoria'] = comissao['product'].apply(categorizar_product)

            # Função para calcular a soma condicional
            def soma_condicional(partner, categoria, dataframe):
                filtro = (dataframe['partner'] == partner) & (dataframe['categoria'] == categoria)
                return dataframe[filtro]['commission_value'].sum()

            # Calcular a soma condicional para cada linha do DataFrame financeiro
            financeiro['Valor_Bruto'] = financeiro.apply(
                lambda x: soma_condicional(x['Parceiro'], x['Observacao'], comissao), axis=1)

            # Função para calcular 'Valor_IR' com base em 'Regime_Tributario'
            def calcular_valor_ir(row):
                if row['Regime_Tributario'] == 'Não Optante pelo Simples Nacional':
                    return row['Valor_Bruto'] * 0.015
                else:
                    return 0

            # Aplicar a função para calcular 'Valor_IR' com base em 'Regime_Tributario'
            financeiro['Valor_IR'] = financeiro.apply(calcular_valor_ir, axis=1)
            financeiro['A_creditar'] = financeiro['Valor_Bruto'] - financeiro['Valor_IR']
            financeiro['Data_do_Credito'] = data_formatada
            financeiro['A_creditar'] = financeiro['A_creditar'].round(2)
            # Exclui os valores que estão com 0
            financeiro = financeiro[financeiro['Valor_Bruto'] != 0].reset_index(drop=True)
            timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            nome_arquivo_financeiro = f"iCred_Lote_{timestamp}.xlsx"

            financeiro.to_excel(nome_arquivo_financeiro, index=False)

            # Criar o link de download para o arquivo 'financeiro'
            with open(nome_arquivo_financeiro, 'rb') as file:
                file_content_financeiro = file.read()
                href_financeiro = f'<a href="data:application/octet-stream;base64,{base64.b64encode(file_content_financeiro).decode()}" ' \
                                  f'download="{nome_arquivo_financeiro}">Clique aqui para baixar o lote financeiro</a>'

            # Mostrar o link de download para 'financeiro' na interface do Streamlit
            st.markdown(href_financeiro, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




