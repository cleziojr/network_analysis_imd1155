from functions.functions import processa_dados, constroi_rede, calcula_estatisticas_rede, cria_subredes

dados = Dados(path_data=r"data")
df = dados.processa_dados(2023)

rede_comercial = Rede(df=df)
rede_comercial.constroi_rede()
rede_comercial.calcula_estatisticas_rede(10, 10)
rede_comercial.cria_subredes(10)

