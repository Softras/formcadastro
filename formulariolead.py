import streamlit as st
import pandas as pd
from datetime import datetime
import os
from time import sleep
import pyautogui as auto

DATAINICIAL = datetime(1950,1,1)
DATAFINAL = datetime(2016,12,1)
#6575 dias de 18 anos para calulo de limite

# Função para adicionar CSS personalizado
def add_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Aplica o CSS personalizado à aplicação
add_css('styles.css')

#Ler as base de dados Preços
precos = pd.read_csv('precos.csv', sep=";", encoding='utf-8')

#obter lista de cursos da base
coluna = precos['Modulo ou Trilhas']

#Ler as bases de dados Leads
base = pd.read_csv('basededadoslead.csv', sep=";", encoding='utf-8')

#Função para gravar dados
def gravar_dados(nome, doc, tel, data, endereco, cidade, bairro, cep,
                 nome2, doc2, tel2, data2, endereco2, cidade2, bairro2, cep2, curso, desejo):
    dados = {'Nome_responsavel': [nome], 'CPFRG_Aluno': [doc], 'WhatsApp_Aluno': [tel], 'Nascimento_Aluno': [data], 
             'Endereco_Aluno': [endereco], 'Cidade_Aluno': [cidade], 'Bairro_Aluno': [bairro], 'Cep_Aluno': [cep],
             'Nome_Responsavel': [nome2], 'CPFRG_Responsavel': [doc2], 'WhatsApp_Responsavel': [tel2], 
             'Nascimento_Responsavel': [data2], 'Endereco_Responsavel': [endereco2], 'Cidade_Responsavel': [cidade2], 
             'Bairro_Responsavel': [bairro2], 'Cep_Responsavel': [cep2], 'Curso_Selecionado': [curso], "Desejo_Selecionado": [desejo]}
    
    #cadastrar os dados no arquivo
    df = pd.DataFrame(dados)
    st.balloons() 
    # Checa se o arquivo já existe
    if os.path.isfile('basededadoslead.csv'):
        df.to_csv('basededadoslead.csv', mode='a', header=False, index=False, sep=';')
    else:
        df.to_csv('basededadoslead.csv', index=False)    

def limpardados():
    auto.press('f5')

#Função principal
def main():
    #st.caption("Cadastro para receber informações dos treinamentos")
    st.title("Formulário de Visita/Matrícula")
    # Área de Aluno
    st.subheader("Dados de cadastro do Aluno")

    col1, col2, col3 = st.columns(3)
    with col1:
        # Obrigar Dados de Nome e Telefone
        nome_aluno = st.text_input("Nome:..", key="nome_aluno")
        cpf_rg_aluno = st.text_input("CPF/RG:..", key="cpf_rg_aluno")
        whatsapp_aluno = st.text_input("WhatsApp:..", key="whatsapp_aluno")
    with col2:
        data_nascimento_aluno = st.date_input("Data de Nascimento:..", key="data_nascimento_aluno", value=DATAINICIAL, 
                                            min_value=DATAINICIAL, max_value=DATAFINAL, format="DD/MM/YYYY")
        endereco_aluno = st.text_input("Endereço:..", key="endereco_aluno")
        cidade_aluno = st.text_input("Cidade:..", key="cidade_aluno")
    with col3:
        bairro_aluno = st.text_input("Bairro:..", key="bairro_aluno")
        cep_aluno = st.text_input("CEP:..", key="cep_aluno")

    # Área de Responsável
    st.subheader("Dados de cadastro do Responsável")

    col1, col2, col3 = st.columns(3)
    with col1:
        nome_responsavel = st.text_input("Nome:..", key="nome_responsavel")
        cpf_rg_responsavel = st.text_input("CPF/RG:..", key="cpf_rg_responsavel")
        whatsapp_responsavel = st.text_input("WhatsApp:..", key="whatsapp_responsavel")
    with col2:
        data_nascimento_responsavel = st.date_input("Data de Nascimento:..", key="data_nascimento_responsavel", 
                                                    value=DATAINICIAL, min_value=DATAINICIAL, max_value=DATAFINAL, 
                                                    format="DD/MM/YYYY")
        endereco_responsavel = st.text_input("Endereço:..", key="endereco_responsavel")
        cidade_responsavel = st.text_input("Cidade:..", key="cidade_responsavel")
    with col3:
        bairro_responsavel = st.text_input("Bairro:..", key="bairro_responsavel")
        cep_responsavel = st.text_input("CEP:..", key="cep_responsavel")  

    # Caixa de listagem
    selecao = st.selectbox('Escolha seu curso de interesse:..', coluna)
    
    st.sidebar.title(":sunglasses: OPÇÕES GRATUITAS")
    st.sidebar.write("")
    
    opcoes = st.sidebar.radio("Escolha a opção desejada", ["1 - Conhecer Escola do Futuro", "2 - Conhecer Métodosde Ensino", 
                              "3 - Ganhar Degustação do Curso", "4 - Conhecer Material Didático", "5 - Saber sobre os valores"],
                              index=False)
    match opcoes[0]:
        case "1":
            desejado = "Marcar uma visita para mostrara escola"
        case "2":
            desejado = "Marcar aula demonstrativa do curso evolua"
        case "3":
            desejado = "Marcar aulas gratuítas do cursos que aluno deseja"
        case "4":
            desejado = "Enviar demosntrativos dos materias de apoio"
        case "5":
            desejado = "Entrar em contato para apresentar os valores"
        case _:
            desejado = "Não foi escolhido uma opção"

  # Aqui você pode adicionar a lógica para salvar os dados do formulário
    if st.button("..:Enviar:.."):
        if nome_aluno and whatsapp_aluno:
            gravar_dados(nome_aluno, cpf_rg_aluno, whatsapp_aluno, data_nascimento_aluno, endereco_aluno, cidade_aluno, 
                         bairro_aluno, cep_aluno, nome_responsavel, cpf_rg_responsavel, whatsapp_responsavel, data_nascimento_responsavel, 
                         endereco_responsavel, cidade_responsavel, bairro_responsavel, cep_responsavel, selecao, desejado)
            st.sidebar.success("Cadastro enviado com sucesso!")
            sleep(1)
            limpardados()
        else:
            st.sidebar.error("Favor cadastrar NOME e TELEFONE do aluno")

if __name__ == '__main__':
    main()
    