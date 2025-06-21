import os
import pandas as pd
import networkx as nx

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
            'ZWE': 'Zimbábue'
        }

    def carrega_dados(self) -> pd.DataFrame:

        df = pd.read_csv(os.path.join(self.path_data, r"hs92_country_country_year.csv"))

        return df
    
    def filtra_dados(self, df) -> pd.DataFrame:

        df = df[df['year'] == 2023]

        return df

    def converte_abreviacoes(self, df) -> pd.DataFrame:
        
        df['country_iso3_code'] = df['country_iso3_code'].str.upper().map(self.nomes_paises).fillna(df['country_iso3_code'])
        df['partner_iso3_code'] = df['partner_iso3_code'].str.upper().map(self.nomes_paises).fillna(df['partner_iso3_code'])
        
        return df
    
    def processa_dados(self) -> pd.DataFrame:

        df = self.carrega_dados()
        df = self.filtra_dados(df=df)
        df = self.converte_abreviacoes(df=df)

        return df
    
class Rede:

    def __init__(self, df = pd.DataFrame):

        self.dados = df
        self.dg = nx.DiGraph()

    def constroi_rede(self) -> nx.DiGraph:

        for row in self.dados.itertuples():
            self.dg.add_edge(row.country_iso3_code, row.partner_iso3_code, abs(row.export_value-row.import_value))

        return self.dg
    
    def analisa_rede(self):

        print(self.dg.degree)
        
        print(self.dg.nodes)
    




