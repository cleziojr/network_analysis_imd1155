import streamlit as st
from functions.functions import Dados, Rede

st.set_page_config(layout="wide")
st.title("Análise de Rede de Comércio Internacional")

dados = Dados(path_data=r"data")
df = dados.processa_dados(2023)

st.write("Dados processados:", df.head())

rede_comercial = Rede(df=df)
rede_comercial.constroi_rede()
rede_comercial.calcula_estatisticas_rede(10, 10)
rede_comercial.cria_subredes(10)

