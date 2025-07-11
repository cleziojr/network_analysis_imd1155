import streamlit as st
from functions.functions import Dados, Rede

st.set_page_config(page_title="Análise de Redes de Comércio", layout="wide")

st.sidebar.header("Configurações")
ano = st.sidebar.slider("Ano de análise", min_value=1995, max_value=2023, value=2023)
quantidade_nos = st.sidebar.number_input("Quantidade de nós (para amostragem da rede)", min_value=10, max_value=238, value=50)
top_n = st.sidebar.number_input("Top N para métricas", min_value=3, max_value=20, value=5)

st.title("Análise de Rede de Comércio Internacional")

dados = Dados(path_data=r"data")
df = dados.processa_dados(ano)

st.write("Dados processados:", df.head())

rede_comercial = Rede(df=df)
rede_comercial.constroi_rede()

tab1, tab2, tab3 = st.tabs(["📊 Métricas", "🌐 Visualização da Rede", "📈 Distribuição de Grau"])

with tab1:
    with st.spinner("Calculando métricas..."):
        rede_comercial.calcula_estatisticas_rede(k=top_n, n=top_n)

with tab2:
    with st.spinner("Gerando subredes..."):
        rede_comercial.cria_subredes(n=top_n)

with tab3:
    with st.spinner("Gerando histogramas..."):
        rede_comercial.exibe_distribuicao_grau()
