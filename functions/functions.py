import os
import pandas as pd
import collections
import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
from pyvis import network as net

class Dados:

    def __init__(self, path_data: str):

        self.path_data = path_data
        self.nomes_paises = {
            'AFG': 'Afeganistão',
            'ALB': 'Albânia',
            'DZA': 'Argélia',
            'AND': 'Andorra',
            'AGO': 'Angola',
            'ATG': 'Antígua e Barbuda',
            'ARG': 'Argentina',
            'ARM': 'Armênia',
            'AUS': 'Austrália',
            'AUT': 'Áustria',
            'AZE': 'Azerbaijão',
            'BHS': 'Bahamas',
            'BHR': 'Bahrein',
            'BGD': 'Bangladesh',
            'BRB': 'Barbados',
            'BLR': 'Bielorrússia',
            'BEL': 'Bélgica',
            'BLZ': 'Belize',
            'BEN': 'Benin',
            'BTN': 'Butão',
            'BOL': 'Bolívia',
            'BIH': 'Bósnia e Herzegovina',
            'BWA': 'Botsuana',
            'BRA': 'Brasil',
            'BRN': 'Brunei',
            'BGR': 'Bulgária',
            'BFA': 'Burkina Faso',
            'BDI': 'Burundi',
            'CPV': 'Cabo Verde',
            'KHM': 'Camboja',
            'CMR': 'Camarões',
            'CAN': 'Canadá',
            'CAF': 'República Centro-Africana',
            'TCD': 'Chade',
            'CHL': 'Chile',
            'CHN': 'China',
            'COL': 'Colômbia',
            'COM': 'Comores',
            'COG': 'Congo',
            'CRI': 'Costa Rica',
            'CIV': 'Costa do Marfim',
            'HRV': 'Croácia',
            'CUB': 'Cuba',
            'CYP': 'Chipre',
            'CZE': 'República Tcheca',
            'DNK': 'Dinamarca',
            'DJI': 'Djibuti',
            'DMA': 'Dominica',
            'DOM': 'República Dominicana',
            'ECU': 'Equador',
            'EGY': 'Egito',
            'SLV': 'El Salvador',
            'GNQ': 'Guiné Equatorial',
            'ERI': 'Eritreia',
            'EST': 'Estônia',
            'SWZ': 'Essuatíni',
            'ETH': 'Etiópia',
            'FJI': 'Fiji',
            'FIN': 'Finlândia',
            'FRA': 'França',
            'GAB': 'Gabão',
            'GMB': 'Gâmbia',
            'GEO': 'Geórgia',
            'DEU': 'Alemanha',
            'GHA': 'Gana',
            'GRC': 'Grécia',
            'GRD': 'Granada',
            'GTM': 'Guatemala',
            'GIN': 'Guiné',
            'GNB': 'Guiné-Bissau',
            'GUY': 'Guiana',
            'HTI': 'Haiti',
            'HND': 'Honduras',
            'HUN': 'Hungria',
            'ISL': 'Islândia',
            'IND': 'Índia',
            'IDN': 'Indonésia',
            'IRN': 'Irã',
            'IRQ': 'Iraque',
            'IRL': 'Irlanda',
            'ISR': 'Israel',
            'ITA': 'Itália',
            'JAM': 'Jamaica',
            'JPN': 'Japão',
            'JOR': 'Jordânia',
            'KAZ': 'Cazaquistão',
            'KEN': 'Quênia',
            'KIR': 'Kiribati',
            'PRK': 'Coreia do Norte',
            'KOR': 'Coreia do Sul',
            'XKX': 'Kosovo',
            'KWT': 'Kuwait',
            'KGZ': 'Quirguistão',
            'LAO': 'Laos',
            'LVA': 'Letônia',
            'LBN': 'Líbano',
            'LSO': 'Lesoto',
            'LBR': 'Libéria',
            'LBY': 'Líbia',
            'LIE': 'Liechtenstein',
            'LTU': 'Lituânia',
            'LUX': 'Luxemburgo',
            'MDG': 'Madagascar',
            'MWI': 'Malawi',
            'MYS': 'Malásia',
            'MDV': 'Maldivas',
            'MLI': 'Mali',
            'MLT': 'Malta',
            'MHL': 'Ilhas Marshall',
            'MRT': 'Mauritânia',
            'MUS': 'Maurício',
            'MEX': 'México',
            'FSM': 'Micronésia',
            'MDA': 'Moldávia',
            'MCO': 'Mônaco',
            'MNG': 'Mongólia',
            'MNE': 'Montenegro',
            'MAR': 'Marrocos',
            'MOZ': 'Moçambique',
            'MMR': 'Mianmar',
            'NAM': 'Namíbia',
            'NRU': 'Nauru',
            'NPL': 'Nepal',
            'NLD': 'Países Baixos',
            'NZL': 'Nova Zelândia',
            'NIC': 'Nicarágua',
            'NER': 'Níger',
            'NGA': 'Nigéria',
            'MKD': 'Macedônia do Norte',
            'NOR': 'Noruega',
            'OMN': 'Omã',
            'PAK': 'Paquistão',
            'PLW': 'Palau',
            'PAN': 'Panamá',
            'PNG': 'Papua-Nova Guiné',
            'PRY': 'Paraguai',
            'PER': 'Peru',
            'PHL': 'Filipinas',
            'POL': 'Polônia',
            'PRT': 'Portugal',
            'QAT': 'Catar',
            'ROU': 'Romênia',
            'RUS': 'Rússia',
            'RWA': 'Ruanda',
            'KNA': 'São Cristóvão e Névis',
            'LCA': 'Santa Lúcia',
            'VCT': 'São Vicente e Granadinas',
            'WSM': 'Samoa',
            'SMR': 'San Marino',
            'STP': 'São Tomé e Príncipe',
            'SAU': 'Arábia Saudita',
            'SEN': 'Senegal',
            'SRB': 'Sérvia',
            'SYC': 'Seicheles',
            'SLE': 'Serra Leoa',
            'SGP': 'Singapura',
            'SVK': 'Eslováquia',
            'SVN': 'Eslovênia',
            'SLB': 'Ilhas Salomão',
            'SOM': 'Somália',
            'ZAF': 'África do Sul',
            'SSD': 'Sudão do Sul',
            'ESP': 'Espanha',
            'LKA': 'Sri Lanka',
            'SDN': 'Sudão',
            'SUR': 'Suriname',
            'SWE': 'Suécia',
            'CHE': 'Suíça',
            'SYR': 'Síria',
            'TWN': 'Taiwan',
            'TJK': 'Tajiquistão',
            'TZA': 'Tanzânia',
            'THA': 'Tailândia',
            'TLS': 'Timor-Leste',
            'TGO': 'Togo',
            'TON': 'Tonga',
            'TTO': 'Trinidad e Tobago',
            'TUN': 'Tunísia',
            'TUR': 'Turquia',
            'TKM': 'Turcomenistão',
            'TUV': 'Tuvalu',
            'UGA': 'Uganda',
            'UKR': 'Ucrânia',
            'ARE': 'Emirados Árabes Unidos',
            'GBR': 'Reino Unido',
            'USA': 'Estados Unidos',
            'URY': 'Uruguai',
            'UZB': 'Uzbequistão',
            'VUT': 'Vanuatu',
            'VAT': 'Vaticano',
            'VEN': 'Venezuela',
            'VNM': 'Vietnã',
            'YEM': 'Iêmen',
            'ZMB': 'Zâmbia',
            'ZWE': 'Zimbábue',
            'ATA': 'Antártida',
            'ASM': 'Samoa Americana',
            'BMU': 'Bermudas',
            'BVT': 'Ilha Bouvet',
            'IOT': 'Território Britânico do Oceano Índico',
            'VGB': 'Ilhas Virgens Britânicas',
            'CYM': 'Ilhas Cayman',
            'COD': 'República Democrática do Congo',
            'COK': 'Ilhas Cook',
            'CXR': 'Ilha Christmas',
            'CCK': 'Ilhas Cocos (Keeling)',
            'FRO': 'Ilhas Faroé',
            'FLK': 'Ilhas Malvinas (Falkland)',
            'SGS': 'Ilhas Geórgia do Sul e Sandwich do Sul',
            'PYF': 'Polinésia Francesa',
            'ATF': 'Terras Austrais e Antárticas Francesas',
            'PSE': 'Palestina',
            'GIB': 'Gibraltar',
            'GRL': 'Groenlândia',
            'GUM': 'Guam',
            'HMD': 'Ilha Heard e Ilhas McDonald',
            'HKG': 'Hong Kong',
            'MAC': 'Macau',
            'MSR': 'Montserrat',
            'CUW': 'Curaçao',
            'ABW': 'Aruba',
            'SXM': 'São Martinho (parte holandesa)',
            'BES': 'Bonaire, Santo Eustáquio e Saba',
            'NCL': 'Nova Caledônia',
            'NIU': 'Niue',
            'NFK': 'Ilha Norfolk',
            'MNP': 'Ilhas Marianas do Norte',
            'UMI': 'Ilhas Menores Distantes dos EUA',
            'PCN': 'Ilhas Pitcairn',
            'BLM': 'Saint Barthélemy',
            'SHN': 'Santa Helena',
            'AIA': 'Anguilla',
            'SPM': 'Saint Pierre e Miquelon',
            'ESH': 'Saara Ocidental',
            'TKL': 'Tokelau',
            'TCA': 'Ilhas Turcas e Caicos',
            'WLF': 'Wallis e Futuna',
            'ANS': 'Antilhas Holandesas'
        }

    def carrega_dados(self) -> pd.DataFrame:

        # Carrega o conjunto de dados e converte para um DataFrame
        df = pd.read_csv(os.path.join(self.path_data, r"hs92_country_country_year.csv"))

        return df
    
    def filtra_dados(self, df: pd.DataFrame, ano: int) -> pd.DataFrame:

        # Filtra o conjunto de dados com base no valor do ano recebido como parâmetro
        df = df[df['year'] == ano]

        return df

    def converte_abreviacoes(self, df: pd.DataFrame) -> pd.DataFrame:
        
        # Converte abreviações (chaves do dicionário) para os nomes completos dos países (valores do dicionário) nas colunas
        # do DataFrame que possuíam as abreviações
        df['country_iso3_code'] = df['country_iso3_code'].str.upper().map(self.nomes_paises).fillna(df['country_iso3_code'])
        df['partner_iso3_code'] = df['partner_iso3_code'].str.upper().map(self.nomes_paises).fillna(df['partner_iso3_code'])
        
        return df
    
    def processa_dados(self, ano: int) -> pd.DataFrame:

        df = self.carrega_dados()
        df = self.filtra_dados(df=df, ano=ano)
        df = self.converte_abreviacoes(df=df)

        return df
    
class Rede:

    def __init__(self, df = pd.DataFrame):

        # Inicializa a instância da classe
        self.dados = df
        self.dg = nx.DiGraph()

    def constroi_rede(self) -> nx.DiGraph:

        # Altere o valor do parâmetro 'n' da função 'sample()' para acrescentar ou reduzir a quantidade de nós da sua rede
        # Considerando o conjunto de dados atual, você pode ter uma rede constituída de no máximo 238 nós.
        for country_id, country in self.dados[['country_id', 'country_iso3_code']].drop_duplicates().sample(n=50).values:
            self.dg.add_node(node_for_adding=country_id, label=country)

        # Adição de conexões entre os nós com base no conjunto de dados (dois nós - países - estão conectados se possuem relações econômicas)
        for row in self.dados.itertuples():
            if ((row.country_id in self.dg.nodes) and (row.partner_country_id in list(self.dg.nodes))):
                #self.dg.add_edge(row.country_id, row.partner_country_id, weight=abs(row.export_value - row.import_value))
                self.dg.add_edge(row.country_id, row.partner_country_id)

        return self.dg
    
    def exibe_rede(self, g: nx.DiGraph, cabecalho: str, nome_arquivo_rede: str) -> None:

        # Função criada para facilitar a criação paramétrica das visualizações utilizando pyviz por meio do paradigma orientado a objetos
        rede = net.Network(bgcolor='#ffffff', font_color='black', height='800px', width='1200px', heading=cabecalho, directed=True, neighborhood_highlight=True, select_menu=True, filter_menu=True, notebook=True, cdn_resources='remote')
        rede.from_nx(g)
        rede.show_buttons(filter_=True)
        rede.show(nome_arquivo_rede)
        st.components.v1.html(open(nome_arquivo_rede, "r", encoding="utf-8").read(), height=1200, scrolling=True)


    def calcula_metricas_centralidade(self) -> None:

        # Cálculo de métricas de centralidade
        self.centralidade_intermediacao= nx.betweenness_centrality(self.dg)
        self.centralidade_autovetor = nx.eigenvector_centrality(self.dg)
        self.centralidade_grau = nx.degree_centrality(self.dg)
        self.centralidade_proximidade = nx.closeness_centrality(self.dg)

    def calcula_propriedades_rede(self, k: int, n: int) -> None:

        # Cálculo e identificação de propriedades/atributos da rede

        # Densidade da rede
        # Consiste na divisão da quantidade de arestas existentes pela quantidade de arestas possíveis, fornecendo uma noção
        # da conectividade do grafo de forma holística
        self.densidade = nx.density(self.dg)

        # Assortatividade
        # Conceito associado tanto aos tipos de padrões de em relação ao grau quanto ao modo pela qual se originam as conexões
        self.assortatividade = nx.degree_assortativity_coefficient(self.dg)

        # Coeficiente de agrupamento global
        # Calcula a probabilidade de quaisquer pares de nós vizinhos a um determinado nó estarem conectados entre si (formando um clique/triângulo)
        self.coeficiente_agrupamento_global = nx.average_clustering(self.dg)

        # As duas métricas a seguir exibem a sequência de nós com maior e menor centralidade de grau, respectivamente
        self.componentes_fortemente_conectados = sorted(self.centralidade_grau, key=self.centralidade_grau.get, reverse=True)[:k] # Substitua 'k' por outro valor, caso deseje restringir ou ampliar o ranking
        self.componentes_fracamente_conectados = sorted(self.centralidade_grau, key=self.centralidade_grau.get)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking

        # Coeficiente de agrupamento local
        # Como estou passando a rede completa como parâmetro, etorna um dicionário contendo o coeficiente de agrupamento local de cada nó
        self.clustering = nx.clustering(self.dg)
    
    def exibe_distribuicao_grau(self) -> None:

        # Uso do módulo 'collections' para contar a frequência dos graus dos nós
        sequencia_grau = sorted([d for n, d in self.dg.degree()], reverse=True)
        degreeCount = collections.Counter(sequencia_grau)
        deg, cnt = zip(*degreeCount.items())

        # Criação do histograma para visualizar a distribuição do grau dos nós pertencentes à rede em questão
        fig, ax = plt.subplots()
        plt.bar(deg, cnt, width=0.80, color='b')
        plt.title("Histograma de distribuição do grau dos nós")
        plt.ylabel("Frequência")
        plt.xlabel("Grau")
        st.pyplot(fig)

    def cria_subrede_centralidade_grau(self, n: int) -> None:

        # Subrede dos nós com maior centralidade do grau
        maiores_centralidades_grau = sorted(self.centralidade_grau, key=self.centralidade_grau.get, reverse=True)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_dc = self.dg.subgraph(maiores_centralidades_grau)
        self.exibe_rede(g=subgrafo_dc, cabecalho='Nós com maiores centralidades de grau', nome_arquivo_rede='degree_centrality.html')

    def cria_subrede_centralidade_autovetor(self, n: int) -> None:

        # Subrede dos nós com maior centralidade do autovetor
        maiores_centralidades_autovetor = sorted(self.centralidade_autovetor, key=self.centralidade_autovetor.get, reverse=True)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_ec = self.dg.subgraph(maiores_centralidades_autovetor)
        self.exibe_rede(g=subgrafo_ec, cabecalho='Nós com maiores centralidades de autovetor', nome_arquivo_rede='eigenvector_centrality.html')

    def cria_subrede_centralidade_intermediacao(self, n: int) -> None:

        # Subrede dos nós com maior centralidade de intermediação
        maiores_centralidades_intermediacao = sorted(self.centralidade_intermediacao, key=self.centralidade_intermediacao.get, reverse=True)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_bc = self.dg.subgraph(maiores_centralidades_intermediacao)
        self.exibe_rede(g=subgrafo_bc, cabecalho='Nós com maiores centralidades de intermediação', nome_arquivo_rede='betweenness_centrality.html')

    def cria_subrede_centralidade_proximidade(self, n: int) -> None:

        # Subrede dos nós com maior centralidade de proximidade
        maiores_centralidades_proximidade = sorted(self.centralidade_proximidade, key=self.centralidade_proximidade.get, reverse=True)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_cc = self.dg.subgraph(maiores_centralidades_proximidade)
        self.exibe_rede(g=subgrafo_cc, cabecalho='Nós com maiores centralidades de proximidade', nome_arquivo_rede='closeness_centrality.html')

    def cria_subrede_fortemente_conectada(self) -> None:

        # Subrede dos nós mais fortemente conectados
        subgrafo_scc = self.dg.subgraph(self.componentes_fortemente_conectados)
        self.exibe_rede(g=subgrafo_scc, cabecalho='Nós mais fortemente conectados', nome_arquivo_rede='scc.html')

    def cria_subrede_fracamente_conectada(self) -> None:

        # Subrede dos nós mais fracamente conectados
        subgrafo_wcc = self.dg.subgraph(self.componentes_fracamente_conectados)
        self.exibe_rede(g=subgrafo_wcc, cabecalho='Nós mais fracamente conectados', nome_arquivo_rede='wcc.html')  

    def cria_subrede_fortemente_agrupada(self, n: int) -> None:

        # Subrede dos nós com maiores coeficientes de agrupamento
        maiores_coeficientes_agrupamento = sorted(self.clustering, key=self.clustering.get)[:n] # Substitua n por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_cl_alto = self.dg.subgraph(maiores_coeficientes_agrupamento)
        self.exibe_rede(g=subgrafo_cl_alto, cabecalho='Nós com maiores coeficientes de agrupamento', nome_arquivo_rede='hcc.html')

    def cria_subrede_fracamente_agrupada(self, n: int) -> None:

        # Subrede dos nós com menores coeficientes de agrupamento
        menores_coeficientes_agrupamento = sorted(self.clustering, key=self.clustering.get, reverse=True)[:n] # Substitua 'n' por outro valor, caso deseje restringir ou ampliar o ranking
        subgrafo_cl_baixo = self.dg.subgraph(menores_coeficientes_agrupamento)
        self.exibe_rede(g=subgrafo_cl_baixo, cabecalho='Nós com menores coeficientes de agrupamento', nome_arquivo_rede='lcc.html')

    def calcula_estatisticas_rede(self, k: int, n: int) -> None:

        self.calcula_metricas_centralidade()
        self.calcula_propriedades_rede(k=k, n=n)
        self.exibe_distribuicao_grau()

    def cria_subredes(self, n: int) -> None:
        
        self.cria_subrede_centralidade_grau(n)
        self.cria_subrede_centralidade_autovetor(n)
        self.cria_subrede_centralidade_intermediacao(n)
        self.cria_subrede_centralidade_proximidade(n)
        self.cria_subrede_fortemente_conectada()
        self.cria_subrede_fracamente_conectada()
        self.cria_subrede_fortemente_agrupada(n)
        self.cria_subrede_fracamente_agrupada(n)
    




